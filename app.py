import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image
import os
from datetime import datetime

def create_streamlit_app():
    st.header("Fashion Search Model Analysis")

    # Load all DataFrames
    metrics_df = pd.read_csv('/Users/sammy/Desktop/Shoppin/detailed_metrics_20241129_033725.csv')
    results_df = pd.read_csv('/Users/sammy/Desktop/Shoppin/query_results_20241129_033725.csv')
    
    # Create summary DataFrame
    summary_df = results_df.groupby('Model').agg({
        'Is_Correct_Category': 'mean',
        'Query_Time': 'mean',
        'Similarity_Score': ['mean', 'std']
    }).round(4)

    def load_image(image_path):
        try:
            img = Image.open(image_path)
            max_size = (200, 200)
            img.thumbnail(max_size)
            return img
        except Exception as e:
            st.error(f"Error loading image {image_path}: {str(e)}")
            return None

    # Tabs
    tab = st.selectbox(
        "Select a view",
        ["Model Performance Metrics", "Query Results Visualization", "Summary Analysis", "Raw Data"]
    )

    # Tab 1: Detailed Metrics
    if tab == "Model Performance Metrics":
        st.header("Detailed Model Performance Metrics")
        
        # Performance metrics
        st.subheader("Performance Metrics")
        perf_metrics = metrics_df[['Model', 'Mean Precision', 'Mean Recall', 'F1 Score']]
        
        # Convert string metrics to float for visualization
        for col in ['Mean Precision', 'Mean Recall', 'F1 Score']:
            perf_metrics[col] = perf_metrics[col].astype(float)
        
        st.dataframe(perf_metrics)
        
        # Visualizations
        fig1 = px.bar(perf_metrics.melt(id_vars=['Model'], 
                                      value_vars=['Mean Precision', 'Mean Recall', 'F1 Score']),
                     x='Model', y='value', color='variable',
                     title='Model Performance Comparison',
                     barmode='group')
        st.plotly_chart(fig1)

    # Tab 2: Query Results Visualization
    elif tab == "Query Results Visualization":
    
        st.header("Query Results Visualization")
        
        # Model and Query selection
        col1, col2 = st.columns(2)
        with col1:
            selected_model = st.selectbox("Select Model", sorted(results_df['Model'].unique()))
        with col2:
            selected_query = st.selectbox("Select Query ID", sorted(results_df['Query_ID'].unique()))
        
        # Filter results
        query_results = results_df[
            (results_df['Query_ID'] == selected_query) & 
            (results_df['Model'] == selected_model)
        ].reset_index(drop=True)  # Reset index to ensure proper iteration
        
        if not query_results.empty:
            # Display query image
            query_image_path = query_results.iloc[0]['Query_Image']
            query_category = query_results.iloc[0]['Query_Category']
            
            # Display query section
            st.subheader(f"Query Image (Category: {query_category})")
            query_img = load_image(query_image_path)
            if query_img:
                st.image(query_img, caption="Query Image", width=200)

            # Display retrieved section
            st.subheader("Retrieved Results")
            retrieved_images = st.container()  # Create container for retrieved images
            
            # Create columns for retrieved images
            with retrieved_images:
                cols = st.columns(5)
                for idx in range(5):  # Show all 5 results
                    with cols[idx]:
                        if idx < len(query_results):
                            row = query_results.iloc[idx]
                            retrieved_img = load_image(row['Retrieved_Image'])
                            if retrieved_img:
                                st.image(retrieved_img)
                                st.caption(f"Rank {row['Rank']}\n" +
                                        f"Score: {row['Similarity_Score']:.3f}\n" +
                                        f"Category: {row['Retrieved_Category']}\n" +
                                        f"Match: {'✅' if row['Is_Correct_Category'] else '❌'}")

            # Metrics section
            st.subheader("Performance Metrics")
            metrics_cols = st.columns(4)
            with metrics_cols[0]:
                st.metric("Query Time", f"{query_results['Query_Time'].iloc[0]:.4f} s")
            with metrics_cols[1]:
                accuracy = query_results['Is_Correct_Category'].mean()
                st.metric("Accuracy", f"{accuracy:.2%}")
            with metrics_cols[2]:
                avg_similarity = query_results['Similarity_Score'].mean()
                st.metric("Avg Similarity", f"{avg_similarity:.3f}")
            with metrics_cols[3]:
                correct_retrievals = query_results['Is_Correct_Category'].sum()
                st.metric("Correct Retrievals", f"{correct_retrievals}/5")

            # Results table
            st.subheader("Detailed Results")
            results_table = query_results[['Rank', 'Retrieved_Category', 
                                        'Similarity_Score', 'Is_Correct_Category']]
            st.dataframe(results_table)

    # Tab 3: Summary Analysis
    elif tab == "Summary Analysis":
        st.header("Summary Analysis")
        
        # Overall model performance
        st.subheader("Model Performance Summary")
        st.dataframe(summary_df)
        
        # Category-wise analysis
        st.subheader("Category-wise Performance")
        cat_perf = results_df.groupby(['Model', 'Query_Category'])['Is_Correct_Category'].mean().unstack()
        st.dataframe(cat_perf)
        
        # Visualizations
        fig2 = px.box(results_df, x='Model', y='Similarity_Score', 
                     title='Similarity Score Distribution by Model')
        st.plotly_chart(fig2)
        
        fig3 = px.box(results_df, x='Model', y='Query_Time',
                     title='Query Time Distribution by Model')
        st.plotly_chart(fig3)

    # Tab 4: Raw Data
    elif tab == "Raw Data":
        st.header("Raw Data")
        
        data_option = st.selectbox(
            "Select Dataset",
            ["Detailed Metrics", "Query Results", "Summary"]
        )
        
        if data_option == "Detailed Metrics":
            st.dataframe(metrics_df)
        elif data_option == "Query Results":
            st.dataframe(results_df)
        else:
            st.dataframe(summary_df)

    # Download buttons in sidebar
    st.sidebar.header("Download Data")
    
    for name, data in {
        "Detailed Metrics": metrics_df,
        "Query Results": results_df,
        "Summary": summary_df
    }.items():
        st.sidebar.download_button(
            f"Download {name}",
            data.to_csv(index=False).encode('utf-8'),
            f"{name.lower().replace(' ', '_')}.csv",
            "text/csv",
            key=f'download-{name.lower().replace(" ", "-")}'
        )

if __name__ == "__main__":
    create_streamlit_app()
