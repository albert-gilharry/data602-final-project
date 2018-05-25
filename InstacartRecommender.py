import pandas as pd
import graphlab as gl


orderData = pd.read_csv("Data/orders.csv")
orderProductData = pd.read_csv("Data/order_products__train.csv")
actions = pd.merge(orderData, orderProductData, on="order_id", how="outer")

actionsTraining = actions[ actions["eval_set"] == "train"]
actionsTraining = actionsTraining.dropna(subset=['product_id'])
actionsTraining = actionsTraining[["user_id", "product_id"]]
actionsTraining.columns = ['user_id', 'item_id'  ]
actionsTraining["item_id"] = actionsTraining["item_id"].astype(int)
sf=gl.SFrame(actionsTraining)

#Item to Item similarity recommender
item_similarity_recommender = gl.recommender.item_similarity_recommender.create(sf)

#Top K recommendations for the model
#here we calculate the top k recommendation for each user. 
k=5
item_similarity_top_k = item_similarity_recommender.recommend(k=k)

#print the recommendation for the first user.
print (item_similarity_top_k[item_similarity_top_k['user_id'] == 1 ])

#save the model in file.
item_similarity_top_k.save('Data/item_similarity_top_5_model')
