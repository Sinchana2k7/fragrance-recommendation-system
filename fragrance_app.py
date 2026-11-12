import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.metrics.pairwise import cosine_similarity
from html import escape


st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600;700&family=DM+Sans:wght@400;500;600&display=swap');


/* =========================================
   1. COLOR PALETTE & GENERAL STYLING
   ========================================= */

:root {
    --forest: #030D07;
    --plum: #301224;
    --button-plum: #6E214A;
    --rose: #C47A99;
    --ivory: #EDEBE4;
    --cream: #EDDEC5;
}

.stApp {
    background-color: var(--forest);
    color: var(--ivory);
}

html, body, .stApp,
[data-testid="stWidgetLabel"],
[data-testid="stMarkdownContainer"],
button, input, p, label {
    font-family: 'DM Sans', sans-serif !important;
}

h1, h2, h3 {
    font-family: 'Cormorant Garamond', Georgia, serif !important;
    color: var(--ivory);
    font-weight: 600;
}

.block-container {
    max-width: 1120px;
    padding-top: 2.5rem;
    padding-bottom: 4rem;
}


/* =========================================
   2. HOMEPAGE HERO
   ========================================= */

.hero-frame {
    position: relative;
    max-width: 950px;
    margin: 10px auto 48px;
    padding: 65px 36px;

    background: transparent;
    border: 1px solid var(--rose);
    outline: 1px solid rgba(196,122,153,0.35);
    outline-offset: -10px;
    border-radius: 10px;

    text-align: center;
    box-sizing: border-box;
}

.hero-kicker {
    font-family: 'DM Sans', sans-serif;
    font-size: 12px;
    letter-spacing: 0.28em;
    text-transform: uppercase;
    color: var(--cream);
    margin-bottom: 18px;
}

.hero-frame h1 {
    font-family: 'Cormorant Garamond', Georgia, serif !important;
    font-size: clamp(48px, 7vw, 78px) !important;
    font-weight: 600;
    line-height: 1.05;
    margin: 0 0 18px !important;
    color: var(--ivory);
    text-align: center;
}

.hero-subtext,
.hero-frame p {
    font-family: 'DM Sans', sans-serif !important;
    font-size: 17px !important;
    line-height: 1.6;
    color: var(--cream);
    text-align: center;
    margin: 0 !important;
}


/* =========================================
   3. HOMEPAGE SECTION LABELS
   ========================================= */

.section-label {
    font-family: 'DM Sans', sans-serif !important;
    font-size: 12px;
    letter-spacing: 0.25em;
    text-transform: uppercase;
    text-align: center;
    color: var(--rose);

    margin: 12px auto 30px;
}


/* =========================================
   4. HOMEPAGE DISCOVERY OPTIONS
   ========================================= */

.scent-choice {
    width: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;

    gap: 12px;
    margin: 0 auto 20px;
    padding: 0;
    box-sizing: border-box;
}

.scent-choice h3 {
    font-family: 'Cormorant Garamond', Georgia, serif !important;
    font-size: 34px !important;
    font-weight: 600 !important;
    line-height: 1.15 !important;

    width: 100%;
    height: auto !important;
    margin: 0 !important;
    padding: 0 !important;
    text-align: center !important;
}

.scent-choice p {
    font-family: 'DM Sans', sans-serif !important;
    font-size: 16px !important;
    line-height: 1.6 !important;

    color: var(--cream);
    width: 100%;
    max-width: 340px !important;
    height: auto !important;
    margin: 0 auto !important;
    padding: 0 !important;
    text-align: center !important;
}

/* Decorative divider between discoveries */
.choice-divider {
    width: 90px;
    height: 1px;
    background-color: var(--rose);
    margin: 36px auto 42px;
}


/* =========================================
   5. BUTTON STYLING
   ========================================= */

.stButton button {
    background-color: var(--button-plum) !important;
    color: var(--ivory) !important;

    border: 1px solid var(--rose) !important;
    border-radius: 999px !important;

    font-family: 'DM Sans', sans-serif !important;
    font-size: 15px !important;
    font-weight: 500 !important;

    min-height: 50px;
    padding: 10px 26px !important;

    white-space: nowrap;
    transition: background-color 0.2s ease,
                border-color 0.2s ease,
                transform 0.2s ease;
}

.stButton button:hover {
    background-color: var(--plum) !important;
    color: var(--ivory) !important;
    border-color: var(--cream) !important;
    transform: translateY(-2px);
}

.stButton button:focus {
    color: var(--ivory) !important;
    border-color: var(--rose) !important;
}

/* Button text shouldn't truncate */
.stButton button p {
    font-family: 'DM Sans', sans-serif !important;
    white-space: nowrap !important;
}


/* =========================================
   6. DECORATIVE DIVIDER & EXPLANATION
   ========================================= */

.ornament-divider {
    text-align: center;
    font-family: 'Cormorant Garamond', Georgia, serif;
    font-size: 25px;
    color: var(--rose);
    margin: 46px auto 22px;
}

.how-it-works {
    font-family: 'DM Sans', sans-serif !important;
    font-size: 15px;
    line-height: 1.8;
    text-align: center;
    color: var(--cream);

    max-width: 680px;
    margin: 0 auto 25px;
}


/* =========================================
   7. PERFUME & NOTES DROPDOWNS
   ========================================= */

[data-baseweb="select"] * {
    font-family: 'DM Sans', sans-serif !important;
}

div[data-baseweb="select"] > div {
    background-color: #302D2B !important;
    border: 1px solid #56504E !important;
    border-radius: 12px !important;
}

div[data-baseweb="select"] input {
    color: var(--ivory) !important;
    -webkit-text-fill-color: var(--ivory) !important;
}

div[data-baseweb="select"] svg {
    fill: var(--ivory) !important;
}


/* =========================================
   8. STANDARD FRAGRANCE RESULT CARDS
   ========================================= */

.perfume-card {
    background-color: var(--plum);
    border: 1px solid var(--rose);
    border-radius: 16px;

    box-sizing: border-box;
    width: 100%;
    height: 245px;
    overflow: hidden;

    padding: 20px;

    display: grid;
    grid-template-rows: 36px minmax(65px, 1fr) auto auto;
    row-gap: 6px;
    align-items: stretch;

    margin: 0 0 14px;
}

.card-header {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    gap: 10px;
    width: 100%;
    min-width: 0;
}

.brand-name {
    font-family: 'DM Sans', sans-serif !important;
    font-size: 15px;
    font-weight: 500;
    line-height: 1.35;
    color: var(--ivory);

    overflow-wrap: anywhere;
}

/* Perfume name */
.perfume-card h2 {
    font-family: 'Cormorant Garamond', Georgia, serif !important;
    font-size: clamp(25px, 2.5vw, 34px) !important;
    font-weight: 600 !important;
    line-height: 1.1 !important;
    color: var(--ivory);

    margin: 0 !important;
    padding: 0 !important;
    overflow-wrap: anywhere;
    align-self: center;
}

/* Similarity & rating */
.perfume-card p {
    font-family: 'DM Sans', sans-serif !important;
    font-size: 14px !important;
    line-height: 1.45 !important;
    color: var(--ivory);

    margin: 0 !important;
    padding: 0 !important;
}

/* First-ranked fragrance */
.top-badge {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;

    background-color: var(--rose);
    color: var(--plum);

    border-radius: 999px;
    padding: 5px 9px;

    font-family: 'DM Sans', sans-serif !important;
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 0.03em;
    white-space: nowrap;
}



/* =========================================
   10. MISCELLANEOUS
   ========================================= */

[data-testid="stDataFrame"] {
    font-family: 'DM Sans', sans-serif !important;
}

/* Streamlit borders (where used) */
div[data-testid="stVerticalBlockBorderWrapper"] {
    border-radius: 16px;
}


/* =========================================
   11. RESPONSIVE STYLING
   ========================================= */

@media (max-width: 700px) {

    .block-container {
        padding-left: 1rem;
        padding-right: 1rem;
    }

    .hero-frame {
        padding: 44px 18px;
    }

    .hero-frame h1 {
        font-size: clamp(40px, 9vw, 58px) !important;
    }

    .scent-choice h3 {
        font-size: 30px !important;
    }

    .scent-choice p {
        max-width: 300px !important;
    }

    .perfume-card {
        height: auto;
        min-height: 245px;
    }

    .perfume-card.has-notes {
        height: auto;
        min-height: 380px;
        grid-template-rows:
            36px
            minmax(65px, 1fr)
            auto
            auto
            minmax(132px, auto);
    }

    .perfume-card h2 {
        font-size: 28px !important;
    }

    .perfume-card.has-notes .shared-notes {
        overflow: visible;
    }

    .how-it-works {
        padding: 0 12px;
    }
}

/* =================================
   SELECTION TEXT
   ================================= */

[data-testid="stWidgetLabel"] p {
    font-size: 17px !important;
}

div[data-baseweb="select"] input,
div[data-baseweb="select"] [role="combobox"] {
    font-size: 18px !important;
}

div[data-baseweb="select"] [data-testid="stMarkdownContainer"] p {
    font-size: 18px !important;
}

/* Dropdown menu options */
[role="listbox"] [role="option"] {
    font-size: 17px !important;
}


/* =================================
   FRAGRANCE CARD TYPOGRAPHY
   ================================= */

.perfume-card h2 {
    font-size: 28px !important;
    line-height: 1.15 !important;
}

.perfume-card .brand-name {
    font-size: 16px !important;
}

.perfume-card p {
    font-size: 15px !important;
    line-height: 1.5 !important;
}


/* =========================================
   UNIFIED RECOMMENDATION CARD DESIGN
   Applies to BOTH recommendation systems
   ========================================= */

/* Matching card dimensions */
.perfume-card.has-notes,
.perfume-card.notes-discovery-card {
    display: flex !important;
    flex-direction: column !important;
    height: auto !important;
    min-height: 340px !important;
    padding: 22px !important;
    gap: 0 !important;
    overflow: visible !important;
    box-sizing: border-box;
}

/* Brand name and badge */
.perfume-card.has-notes .card-header,
.perfume-card.notes-discovery-card .card-header {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    min-height: 30px;
    margin: 0 0 12px !important;
}

/* Perfume titles */
.perfume-card.has-notes h2,
.perfume-card.notes-discovery-card h2 {
    font-size: 28px !important;
    line-height: 1.15 !important;
    min-height: 66px;
    margin: 0 0 12px !important;
    padding: 0 !important;
    align-self: stretch;
}

/* Similarity and rating */
.perfume-card.has-notes .card-stats,
.perfume-card.notes-discovery-card .card-stats {
    display: flex;
    flex-direction: column;
    gap: 5px;
    margin: 0 !important;
    padding: 0 !important;
}

/* Notes section: identical positioning */
.perfume-card.has-notes .shared-notes,
.perfume-card.notes-discovery-card .shared-notes {
    display: flex !important;
    flex-direction: column !important;
    gap: 8px !important;

    margin: 18px 0 0 !important;
    padding: 14px 0 0 !important;

    border-top: 1px solid rgba(196,122,153,0.45);
    overflow: visible !important;
}

/* Both note section headings */
.shared-notes .notes-label {
    font-family: 'DM Sans', sans-serif !important;
    font-size: 11px !important;
    font-weight: 600 !important;
    letter-spacing: 1.2px !important;
    line-height: 1.4 !important;
    text-transform: uppercase;

    color: #EDDEC5;
    margin: 0 !important;
    padding: 0 !important;
}

/* Space before second note category */
.shared-notes .other-notes-label {
    margin-top: 10px !important;
}

/* Pink note tags */
.shared-notes .note-tags {
    display: flex !important;
    flex-wrap: wrap !important;
    align-items: center;
    align-content: flex-start;
    gap: 7px !important;

    margin: 0 !important;
    padding: 0 !important;
    width: 100%;
}

/* Individual tags */
.shared-notes .note-tag {
    display: inline-flex !important;
    align-items: center;
    justify-content: center;

    border: 1px solid #C47A99;
    border-radius: 999px;
    padding: 5px 10px;

    font-family: 'DM Sans', sans-serif !important;
    font-size: 11px !important;
    line-height: 1.35;
    color: #EDEBE4;

    max-width: 100%;
    white-space: normal;
    overflow-wrap: anywhere;
}

/* +X more indicator */
.shared-notes .note-more {
    display: inline-flex;
    align-items: center;

    font-family: 'DM Sans', sans-serif !important;
    font-size: 11px !important;
    color: #C47A99;
    padding: 5px 2px;
}

/* Let long names and notes expand on mobile */
@media (max-width: 700px) {
    .perfume-card.has-notes,
    .perfume-card.notes-discovery-card {
        height: auto !important;
        min-height: 340px !important;
    }

    .perfume-card.has-notes h2,
    .perfume-card.notes-discovery-card h2 {
        min-height: 0;
    }
}

</style>
""", unsafe_allow_html=True)


df = pd.read_csv("data/fra_cleaned.csv", sep=";", encoding="latin1")
df["All_Notes"] = (
    df["Top"].fillna("") + "," +
    df["Middle"].fillna("") + "," +
    df["Base"].fillna(""))
df["All_Notes"] = df["All_Notes"].str.lower().apply(
    lambda x: [note.strip() for note in x.split(",") if note.strip()])
mlb = MultiLabelBinarizer()
note_matrix = mlb.fit_transform(df["All_Notes"])
if "page" not in st.session_state:
    st.session_state.page = "home"
# Homepage
if st.session_state.page == "home":

    st.markdown("""
    <div class="hero-frame">
        <div class="hero-kicker">THE FRAGRANCE ATELIER</div>
        <h1>Find your perfect scent.</h1>
        <p class="hero-subtext">
            A little fragrance magic, made just for you.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-label">TWO WAYS TO DISCOVER</div>', unsafe_allow_html=True)

    
    # First discovery option
    st.markdown("""
    <div class="scent-choice">
        <h3>Your Fragrance Twin</h3>
        <p>Find your next favorite based on a perfume you already love.</p>
    </div>
    """, unsafe_allow_html=True)

    with st.container(horizontal=True, horizontal_alignment="center"):
        if st.button("Explore by Perfume", key="home_perfume"):
            st.session_state.page = "perfume"
            st.rerun()

    st.markdown('<div class="choice-divider"></div>', unsafe_allow_html=True)

    # Second discovery option
    st.markdown("""
    <div class="scent-choice">
        <h3>Discover by Notes</h3>
        <p>Find beautiful fragrances using the notes you adore.</p>
    </div>
    """, unsafe_allow_html=True)

    with st.container(horizontal=True, horizontal_alignment="center"):
        if st.button("Explore by Notes", key="home_notes"):
            st.session_state.page = "notes"
            st.rerun()



    st.markdown('<div class="ornament-divider">✦</div>', unsafe_allow_html=True)

    st.markdown('<div class="section-label">HOW THE MAGIC WORKS</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="how-it-works">
        Explore over 24,000 fragrances through their scent notes.
        Our recommendation models compare fragrance compositions
        to help you discover perfumes that match your taste.
    </div>
    """, unsafe_allow_html=True)

    st.stop()



if st.session_state.page == "perfume":
    if st.button("← Back to Home", key="back_perfume"):
        st.session_state.page = "home"
        st.rerun()

    st.subheader("Find Your Fragrance Twin")
    st.caption(
            "Similarity measures how closely each perfume's fragrance notes "
            "match your selected scent using cosine similarity. "
            "A higher percentage means greater note overlap, "
            "not a guaranteed preference or identical smell."
        )
    
    selected_index = st.selectbox(
        "Choose a perfume you love",
        options=df.index[df["Perfume"].notna()].tolist(),
        format_func=lambda i: (
            f'{str(df.loc[i, "Brand"]).replace("-", " ").title()}'
            f' — {str(df.loc[i, "Perfume"]).replace("-", " ").title()}'
        )
    )
    selected_perfume_notes = set(df.loc[selected_index, "All_Notes"])
    scores = cosine_similarity(
        note_matrix[selected_index:selected_index + 1],
        note_matrix)[0]
    ranked_indices = np.argsort(scores)[::-1]
    ranked_indices = ranked_indices[ranked_indices != selected_index]
    top_four = ranked_indices[:4]
    recommendations = df.iloc[top_four][["Perfume", "Brand", "Rating Value"]].copy()
    recommendations["Similarity Score"] = scores[top_four].round(2)


    if st.button("Find My Matches"):
        st.subheader("Your Fragrance Matches")

        col1, col2 = st.columns(2, gap="medium")

        for i, (perfume_index, perfume) in enumerate(recommendations.iterrows()):
            with (col1 if i % 2 == 0 else col2):

                recommended_notes = set(df.loc[perfume_index, "All_Notes"])

                shared_notes = sorted(
                    selected_perfume_notes & recommended_notes
                )
                other_notes = sorted(recommended_notes - selected_perfume_notes)
                
                
                visible_notes = shared_notes[:3]

                notes_html = " ".join(
                    f'<span class="note-tag">'
                    f'{escape(note.replace("-", " ").title())}'
                    f'</span>'
                    for note in visible_notes
                )

                remaining = len(shared_notes) - len(visible_notes)

                if remaining > 0:
                    notes_html += (
                        f' <span class="note-more">+{remaining} more</span>'
                    )


                # Show up to 3 additional notes
                visible_other = other_notes[:3]

                other_html = " ".join(
                    f'<span class="note-tag">'
                    f'{escape(note.replace("-", " ").title())}'
                    f'</span>'
                    for note in visible_other
                )

                other_remaining = len(other_notes) - len(visible_other)

                if other_remaining > 0:
                    other_html += (
                        f' <span class="note-more">'
                        f'+{other_remaining} more</span>'
                    )

                badge = '<div class="top-badge">#1 MATCH</div>' if i == 0 else ''

                brand = escape(str(perfume["Brand"]).replace("-", " ").title())
                name = escape(str(perfume["Perfume"]).replace("-", " ").title())
                similarity = f'{float(perfume["Similarity Score"]) * 100:.0f}%'
                rating_value = str(perfume["Rating Value"]).replace(",", ".")
                try:
                    rating = f"{float(rating_value):.2f} / 5"
                except ValueError:
                    rating = "Not rated"

                card_html = (
                    f'<div class="perfume-card has-notes">'
                    f'<div class="card-header">'
                    f'<span class="brand-name">{brand}</span>'
                    f'{badge}'
                    f'</div>'
                    f'<h2>{name}</h2>'
                   
                    f'<div class="card-stats">'
                    f'<p>Similarity: {similarity}</p>'
                    f'<p>Rating: {rating}</p>'
                    f'</div>'

                    
                    f'<div class="shared-notes">'
                    f'<div class="notes-label">SHARED NOTES</div>'
                    f'<div class="note-tags">{notes_html}</div>'
                    f'<div class="notes-label other-notes-label">OTHER NOTES TO EXPLORE</div>'
                    f'<div class="note-tags">{other_html or "No additional notes"}</div>'
                    f'</div>'

                    f'</div>'
                )

                st.markdown(card_html, unsafe_allow_html=True)
if st.session_state.page == "notes":

    if st.button("← Back to Home", key="back_notes"):
        st.session_state.page = "home"
        st.rerun()
    st.subheader("Discover by Notes")
    st.write(
        "Choose your favorite fragrance notes to discover "
        "perfumes that match your preferences.")
    selected_notes = st.multiselect(
        "Choose up to 5 fragrance notes",
        options=list(mlb.classes_),
        max_selections=5)
    if st.button("Find My Scent"):
        if not selected_notes:
            st.warning("Please select at least one fragrance note.")

        else:
            user_vector = mlb.transform([selected_notes])

            note_scores = cosine_similarity(
                user_vector,
                note_matrix
            )[0]

            ranked_notes = np.argsort(-note_scores, kind="stable")
            top_notes = ranked_notes[note_scores[ranked_notes] > 0][:4]

            note_recommendations = df.iloc[top_notes][
                ["Perfume", "Brand", "Rating Value"]
            ].copy()

            note_recommendations["Similarity Score"] = (
                note_scores[top_notes].round(2)
            )

            st.subheader("Your Personalized Fragrance Matches")
            st.caption(
                "Similarity compares your selected notes with each perfume's "
                "full note profile using cosine similarity. "
                "A higher percentage indicates a closer note-based match, "
                "not the likelihood that you'll enjoy the fragrance."
            )
        
            col1, col2 = st.columns(2, gap="medium")

            for i, (perfume_index, perfume) in enumerate(note_recommendations.iterrows()):
                with (col1 if i % 2 == 0 else col2):
                
                    # Notes found in this perfume
                    perfume_notes = set(df.loc[perfume_index, "All_Notes"])

                    # Notes matching the user's selections
                    matching_notes = sorted(set(selected_notes) & perfume_notes)

                    # Other notes found in this perfume
                    other_notes = sorted(perfume_notes - set(selected_notes))

                    # Build matching-note tags
                    matching_html = " ".join(
                        f'<span class="note-tag">{escape(note.replace("-", " ").title())}</span>'
                        for note in matching_notes
                    )

                    # Show up to 3 other notes
                    visible_other = other_notes[:3]

                    other_html = " ".join(
                        f'<span class="note-tag">{escape(note.replace("-", " ").title())}</span>'
                        for note in visible_other
                    )

                    remaining = len(other_notes) - len(visible_other)

                    if remaining > 0:
                        other_html += f' <span class="note-more">+{remaining} more</span>'


                    badge = '<div class="top-badge">#1 MATCH</div>' if i == 0 else ''

                    brand = escape(str(perfume["Brand"]).replace("-", " ").title())
                    name = escape(str(perfume["Perfume"]).replace("-", " ").title())
                    similarity = f'{float(perfume["Similarity Score"]) * 100:.0f}%'
                    rating_value = str(perfume["Rating Value"]).replace(",", ".")
                    try:
                        rating = f"{float(rating_value):.2f} / 5"
                    except ValueError:
                        rating = "Not rated"

                    
                    card_html = (
                        f'<div class="perfume-card notes-discovery-card">'
                        f'<div class="card-header">'
                        f'<span class="brand-name">{brand}</span>'
                        f'{badge}'
                        f'</div>'
                        f'<h2>{name}</h2>'
                        f'<div class="card-stats">'
                        f'<p>Similarity: {similarity}</p>'
                        f'<p>Rating: {rating}</p>'
                        f'</div>'
                        f'<div class="shared-notes">'
                        f'<div class="notes-label">MATCHES YOUR NOTES</div>'
                        f'<div class="note-tags">{matching_html}</div>'
                        f'<div class="notes-label other-notes-label">OTHER NOTES TO EXPLORE</div>'
                        f'<div class="note-tags">{other_html}</div>'
                        f'</div>'
                        f'</div>'
                    )


                    st.markdown(card_html, unsafe_allow_html=True)

                    

