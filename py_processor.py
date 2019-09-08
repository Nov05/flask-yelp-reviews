import pandas as pd
import spacy
import scattertext

def processor(df_reviews):
    nlp = spacy.load("en_core_web_sm-2.1.0/en_core_web_sm/en_core_web_sm-2.1.0")

    # add stop words
    with open('stopwords.txt', 'r') as f:
        str = f.read()
        set_stopwords = set(str.split('\n'))
    nlp.Defaults.stop_words |= set_stopwords
 
    corpus = scattertext.CorpusFromPandas(df_reviews, 
                                          category_col='rating', 
                                          text_col='text',
                                          nlp=nlp).build()

    term_freq_df = corpus.get_term_freq_df()
    term_freq_df['highratingscore'] = corpus.get_scaled_f_scores('5.0 star rating')
    term_freq_df['poorratingscore'] = corpus.get_scaled_f_scores('1.0 star rating')

    df_high = term_freq_df.sort_values(by='highratingscore', 
                                       ascending = False)
    df_poor = term_freq_df.sort_values(by='poorratingscore', 
                                       ascending=False)

    df_high = df_high[['highratingscore', 'poorratingscore']]
    df_high['highratingscore'] = round(df_high['highratingscore'], 2)
    df_high['poorratingscore'] = round(df_high['poorratingscore'], 2)
    df_high = df_high.reset_index(drop=False)
    df_high = df_high.head(5)

    df_poor = df_poor[['highratingscore', 'poorratingscore']]
    df_poor['highratingscore'] = round(df_poor['highratingscore'], 2)
    df_poor['poorratingscore'] = round(df_poor['poorratingscore'], 2)
    df_poor = df_poor.reset_index(drop=False)
    df_poor = df_poor.head(5)

    df_terms = pd.concat([df_high, df_poor],
                         ignore_index=True)
    return df_terms