# Fragrance Recommendation System

**A content-based fragrance recommendation system using Python, exploratory data analysis, and cosine similarity.**


**Related Project:** [ScentScout — Interactive Fragrance Discovery App](https://github.com/Sinchana2k7/fragrance-app)
**Live Application:** [Try ScentScout](https://scent-scout.streamlit.app/)

## Project Overview

This project explores how data science and machine learning can be used to analyze fragrance characteristics and develop personalized perfume recommendations.

Using a dataset of **24,063 fragrances**, I analyzed patterns across brands and countries, explored fragrance note popularity and co-occurrence, and developed two content-based recommendation systems using cosine similarity.

The goal was to understand how fragrance compositions can be used to identify similar perfumes and generate recommendations without relying on user purchase histories.


This project served as the foundation for **ScentScout**, an interactive fragrance discovery application built with Streamlit. ScentScout allows users to discover perfumes through similar fragrances or their preferred scent notes. The deployed application is maintained in a separate GitHub repository and uses an updated, price-enriched dataset of 12,369 fragrances.

## Dataset

This project uses the **Fragrantica.com Fragrance Dataset**, published by Olga G (Miufana1) on Kaggle. The data was originally collected from Fragrantica.com and contains information about perfumes, fragrance notes, brands, ratings, and other product characteristics.

The original analysis uses the partially cleaned dataset (`fra_cleaned.csv`), containing **24,063 fragrances and 18 features**.

### Key Variables

- **Perfume:** Fragrance name
- **Brand:** Fragrance manufacturer
- **Country:** Country associated with each fragrance
- **Gender:** Fragrance classification
- **Rating Value:** Average user rating
- **Rating Count:** Number of user ratings
- **Year:** Fragrance release year
- **Top, Middle, and Base:** Fragrance note compositions

**Dataset Source:** [Fragrantica.com Fragrance Dataset](https://www.kaggle.com/datasets/olgagmiufana1/fragrantica-com-fragrance-dataset)

**Dataset License:** CC BY-NC-SA 4.0

The Kaggle dataset includes both raw and partially cleaned versions. I used the partially cleaned version as a starting point and performed additional preprocessing and feature engineering for the analysis and recommendation systems.

The original CSV file is not included in this repository due to its size.

## Tools and Technologies

- **Python:** Data analysis and recommendation system development
- **Pandas and NumPy:** Data cleaning, manipulation, and feature engineering
- **Matplotlib and Seaborn:** Exploratory data visualization
- **Scikit-learn:** MultiLabelBinarizer, cosine similarity, and content-based recommendations
- **Jupyter Notebook:** Development, experimentation, and documentation

## Methodology

### 1. Data Cleaning and Preprocessing

Prepared the fragrance dataset for analysis by examining its structure, handling relevant data quality issues, and organizing fragrance characteristics for further analysis.

The preprocessing steps helped create consistent representations of fragrances for the recommendation systems.

### 2. Exploratory Data Analysis

Explored several patterns in the fragrance industry, including:

- Fragrance distribution across countries and brands
- Popularity and ratings of individual fragrance notes
- Relationships between commonly occurring fragrance notes
- Differences in fragrance characteristics across countries

This analysis helped identify patterns in fragrance compositions and provided context for developing the recommendation systems.

### 3. Feature Engineering

Converted fragrance note compositions into binary feature vectors using `MultiLabelBinarizer`.

Top, middle, and base notes were combined into a representation of each fragrance's scent profile. Each note was encoded as either present (1) or absent (0), allowing fragrances with different compositions to be compared numerically.

These vectors were used as the foundation for both recommendation systems.

### 4. Content-Based Recommendation Systems

Developed two recommendation approaches using cosine similarity to compare fragrance note compositions.

Cosine similarity measures the similarity between two vectors based on their orientation. In this project, it was used to compare the overlap between fragrance note profiles.

#### Model 1: Fragrance-to-Fragrance Recommendation

This system accepts the name of an existing fragrance and identifies other perfumes with similar note compositions.

The process involves:

1. Identifying the selected fragrance in the dataset.
2. Retrieving its encoded fragrance note profile.
3. Calculating cosine similarity against other fragrances.
4. Ranking fragrances by similarity score.
5. Returning the highest-ranked recommendations, along with their brands and ratings.

#### Model 2: Note-Based Recommendation

This system allows users to enter a list of fragrance notes they enjoy.

The process involves:

1. Accepting a list of preferred fragrance notes.
2. Converting those notes into a binary feature vector.
3. Calculating cosine similarity between the user's note profile and fragrances in the dataset.
4. Ranking fragrances by similarity score.
5. Returning fragrances with the highest similarity scores.

Both models rely on fragrance characteristics rather than purchase histories or individual user ratings to generate recommendations.

**Model limitation:** Similarity scores reflect overlap in listed fragrance notes, not guaranteed similarity in scent perception or individual preference. The models do not account for differences in note intensity, formulation, longevity, or skin chemistry.

## Example Recommendations

The following examples were generated using the original recommendation system and its 24,063-fragrance dataset. They are separate from the results produced by the updated Streamlit application.

### Fragrance-to-Fragrance Recommendations

The recommendation system was tested using `champagne-toast`.

Some of the highest-ranked recommendations were:

| Recommended Fragrance | Brand | Similarity Score |
|---|---|---|
| Black Amber Parfum Intense | Zara | 0.55 |
| La Cautiva | Fueguia 1833 | 0.55 |
| Rose Bourbon | Princesse Marina de Bourbon | 0.52 |
| The Wedding Silk Santal 36 | Kayali Fragrances | 0.51 |
| Tommy Bahama Very Cool | Tommy Bahama | 0.45 |

These recommendations were ranked according to similarity in fragrance note composition.

### Note-Based Recommendations

The note-based recommendation system was tested using the preferred notes:

`vanilla`, `oud`, `citrus`

Some of the highest-ranked recommendations included:

| Recommended Fragrance | Brand | Similarity Score |
|---|---|---|
| Awraq Al Oud | Lattafa Perfumes | 0.4364 |
| Elevated Oud | Zara | 0.4364 |
| Oud Oak | Just Jack | 0.4082 |
| Vanille | Molinard | 0.4082 |
| Oudgasm Rose Oud 16 | Kayali Fragrances | 0.4082 |

The results demonstrate how users can receive personalized fragrance recommendations by specifying the scent notes they prefer.

## From Recommendation Model to ScentScout


Following the initial analysis and model development, I expanded the project into **ScentScout**, an interactive fragrance discovery application built with Streamlit.

The application builds on the original content-based recommendation approach while introducing a user-facing interface, reference pricing, and fragrance-family classifications.


### Application Features

- **Fragrance Twin:** Search for an existing perfume and discover fragrances with similar scent notes.
- **Discover by Notes:** Select preferred fragrance notes and receive personalized recommendations.
- **Four Recommendations:** View four ranked fragrance suggestions for each search.
- **Similarity Scores:** Compare recommendations based on fragrance note overlap.
- **Ratings and Reference Prices:** View additional product information alongside recommendations.
- **Searchable Interface:** Find fragrances by name or brand.
- **Interactive Web Application:** Explore recommendations without running Python locally.
- **Fragrance Families:** Explore note-derived classifications such as Floral, Fruity, Gourmand, Spicy, Woody, and Citrus.

### Updated Dataset

The deployed application uses a separately prepared dataset containing:

- **12,369 fragrances**
- **463 distinct fragrance notes**
- Recorded USD reference prices for all included fragrances
- Standardized fragrance notes and cleaned product records

The application dataset differs from the original analysis dataset because of additional data collection, pricing enrichment, and cleaning.

The two repositories are maintained separately to distinguish the underlying data science work from the deployed application.

**Application Repository:** [fragrance-app](https://github.com/Sinchana2k7/fragrance-app)

**Live Application:** [ScentScout](https://scent-scout.streamlit.app/)

## Key Takeaways

- Analyzed a dataset containing over 24,000 fragrances and 18 original features.
- Explored fragrance patterns across countries, brands, and scent compositions.
- Investigated fragrance note popularity, ratings, and co-occurrence relationships.
- Applied feature engineering to transform categorical fragrance notes into numerical representations.
- Built two content-based recommendation systems using cosine similarity.
- Demonstrated how product attributes can generate recommendations without requiring user purchase histories.
- Extended the original recommendation approach into a deployed Streamlit application with an updated, price-enriched dataset.

## Limitations and Future Improvements

While the models demonstrate how content-based recommendation systems can support fragrance discovery, several opportunities remain:

- **Weighted fragrance notes:** Assign different weights to top, middle, and base notes to better represent fragrance composition.
- **Additional fragrance attributes:** Incorporate concentration, release year, or other product characteristics into recommendation scoring.
- **Alternative similarity methods:** Compare cosine similarity with other approaches for representing fragrance relationships.
- **Recommendation evaluation:** Collect structured user feedback to assess perceived recommendation relevance and usefulness.
- **Improved personalization:** Explore user preferences beyond individual fragrance notes.


The original goal of developing an interactive web application has been completed through **ScentScout**. Future development will focus on evaluating recommendation quality, improving personalization, and incorporating user feedback.

## How to Run

### 1. Download the Dataset

Download the dataset from Kaggle:

[Fragrantica.com Fragrance Dataset](https://www.kaggle.com/datasets/olgagmiufana1/fragrantica-com-fragrance-dataset)

Locate the `fra_cleaned.csv` file.

### 2. Organize the Files

Place the dataset in the same directory as the original analysis notebook:

```text
fragrance-recommendation-system/
├── Fragrance_Analysis.ipynb
├── fra_cleaned.csv
├── README.md
└── .gitignore
```

The CSV is required to run the analysis locally but is not included in the GitHub repository.

### 3. Install Dependencies

Install the Python libraries used in the project:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn jupyter
```

### 4. Run the Notebook

Open `Fragrance_Analysis.ipynb` using Jupyter Notebook or VS Code.

The dataset is loaded using:

```python
df = pd.read_csv("fra_cleaned.csv", sep=";", encoding="latin1")
```

Run the notebook cells in order to reproduce the analysis and recommendation results.

## Project Files

- **Fragrance_Analysis.ipynb:** Contains exploratory analysis, preprocessing, visualizations, and the two content-based recommendation systems.
- **README.md:** Project documentation, methodology, results, and instructions.
- **.gitignore:** Excludes unnecessary local files from version control.

## Acknowledgments

The fragrance dataset was published by **Olga G (Miufana1)** on Kaggle, using information collected from Fragrantica.com.

The dataset is credited to its original creator and source under the stated CC BY-NC-SA 4.0 license.
