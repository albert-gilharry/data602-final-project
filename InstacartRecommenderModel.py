import graphlab as gl

class InstacartRecommenderModel:
    
    item_similarity_top_k = 0
    def __init__(self):
        self.item_similarity_top_k = gl.load_sframe('C:\\Users\\naman\\Documents\\Harpreet\\CUNY\\Data_602\\FinalProject\\item_similarity_top_5_model')
        
    def topFiveProductRecommendationForUser( self, user_id):
        recommendedValue = self.item_similarity_top_k[self.item_similarity_top_k['user_id'] == user_id ]
        return list(recommendedValue["item_id"].astype(str))
        

 