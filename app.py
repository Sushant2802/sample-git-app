import streamlit as st

st.title('Campusx')

col1, col2 = st.columns(2)

with col1 :
    st.image('unnamed.png')
with col2:
    st.write("""
        6. Conclusion and Recommendations
        This experiment successfully demonstrated K-Means clustering on the Iris dataset, providing insights into its structure and separability. The following recommendations can enhance clustering performance:

        Use the Elbow Method: Always visualize WCSS to determine an appropriate k.
        Combine with Other Metrics: Supplement the Elbow Method with the Silhouette Score for better validation.
        Consider Advanced Clustering: For datasets with overlapping clusters, algorithms like Gaussian Mixture Models or DBSCAN may provide improved results.
    """)


