from utils.score import LABELS
import numpy as np
from feature_extractor.data_preprocessing import gen_or_load_feats
from feature_extractor.hand_feature_generator import HandFeaturesGenerator
from feature_extractor.polarity_feature_generator import PolarityFeaturesGenerator
from feature_extractor.refuting_feature_generator import RefutingFeaturesGenerator
from feature_extractor.tfidf_feature_generator import TfidfFeatureGenerator
from feature_extractor.word_overlap_feature_generator import WordOverlapFeaturesGenerator
from feature_extractor.svd_feature_generator import SvdFeatureGenerator
from feature_extractor.word_to_vec_feature_generator import Word2VecFeatureGenerator
from feature_extractor.sentiment_feature import SentimentFeatureGenerator


class FeatureGenerator(object):
    def __init__(self,stances,dataset,name):
        self.stances = stances
        self. dataset = dataset
        self.name = name
        self.word_overlap_features = WordOverlapFeaturesGenerator()
        self.refuting_features = RefutingFeaturesGenerator()
        self.polarity_features = PolarityFeaturesGenerator()
        self.hand_features = HandFeaturesGenerator()
        self.tfidf_features = TfidfFeatureGenerator()
        self.svd_features = SvdFeatureGenerator()
        self.word2vec_features = Word2VecFeatureGenerator()
        self.sentiment_features = SentimentFeatureGenerator()


    def generate_features(self):
        h, b, y = [],[],[]

        for stance in self.stances:
            y.append(LABELS.index(stance['Stance']))
            h.append(stance['Headline'])
            b.append(self.dataset.articles[stance['Body ID']])

        X_overlap = gen_or_load_feats(self.word_overlap_features.word_overlap_features, h, b, "features/overlap."+self.name+".npy")
        X_refuting = gen_or_load_feats(self.refuting_features.refuting_features, h, b, "features/refuting."+self.name+".npy")
        X_polarity = gen_or_load_feats(self.polarity_features.polarity_features, h, b, "features/polarity."+self.name+".npy")
        X_hand = gen_or_load_feats(self.hand_features.hand_features, h, b, "features/hand."+self.name+".npy")
        X_tfidf = gen_or_load_feats(self.tfidf_features.tfidf_cosine_features,h,b,"features/tfidf."+self.name+".npy")
        X_svd = gen_or_load_feats(self.svd_features.fit_transform,h,b,"features/svd."+self.name+".npy")
        X_word2vec = gen_or_load_feats(self.word2vec_features.generate_features,h,b,"features/word2vec."+self.name+".npy")
        X_sentiment = gen_or_load_feats(self.sentiment_features.generate_features,h,b,"features/sentiment."+self.name+".npy",False)
        X = np.c_[X_hand, X_polarity, X_refuting, X_overlap, X_tfidf, X_svd, X_word2vec, X_sentiment]
        return X,y

class SingleFeatureGenerator:
    def __init__(self):
        self.word_overlap_features = WordOverlapFeaturesGenerator()
        self.refuting_features = RefutingFeaturesGenerator()
        self.polarity_features = PolarityFeaturesGenerator()
        self.hand_features = HandFeaturesGenerator()
        self.tfidf_features = TfidfFeatureGenerator()
        self.svd_features = SvdFeatureGenerator()
        self.word2vec_features = Word2VecFeatureGenerator()
        self.sentiment_features = SentimentFeatureGenerator()

    def generate_features(self, headline, body):
        h, b = [headline], [body]

        features_list = [
            self.word_overlap_features.word_overlap_features(h, b),
            self.refuting_features.refuting_features(h, b),
            self.polarity_features.polarity_features(h, b),
            self.hand_features.hand_features(h, b),
            self.tfidf_features.tfidf_cosine_features(h, b),
            self.svd_features.fit_transform(h, b),
            self.word2vec_features.generate_features(h, b)
        ]

        filtered_features = []
        for feature in features_list:
            if feature is not None and len(feature) > 0:
                np_feature = np.array(feature)
                if np_feature.size > 0:
                    filtered_features.append(np_feature)

        if filtered_features:
            X = np.concatenate(filtered_features, axis=1)
        else:
            X = np.zeros((1, 10)) 

        return X