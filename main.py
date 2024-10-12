import pandas as pd
import features
import regexParser
import mongoPusher
# data1=features.Features("rakshith", "rakshith.dope@gmail.com", "alphanimble")

df = pd.read_csv("data.csv")
emailDf = pd.DataFrame(df.iloc[:,1])
emailDf.to_csv("emails.csv",index=False)
parsed_data_list = []

for index, row in emailDf.iterrows():
    obj=features.Features()
    obj.message_id=regexParser.extract_message_id(row['message'])
    obj.sender_email = regexParser.extract_sender_email(row['message']) 
    obj.reciever_email = regexParser.extract_reciever_email(row['message']) 
    obj.sender_org = regexParser.extract_sender_org(row['message']) 
    obj.reciever_org = regexParser.extract_reciever_org(row['message']) 
    obj.body = regexParser.extract_body(row['message']) 
    obj.date = regexParser.extract_date(row['message']) 
    parsed_data_list.append(obj)

mongoPusher.add_to_mongodb_atlas(parsed_data_list[1])
# with open("output.json") as json_file:
#     json_df=pd.read_json(json_file)
# json_df.to_excel("extracted_data.xlsx",index=False)


