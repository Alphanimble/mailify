import pandas as pd
import features
import regerParser
# data1=features.Features("rakshith", "rakshith.dope@gmail.com", "alphanimble")

df = pd.read_csv("data.csv")
emailDf = pd.DataFrame(df.iloc[:,1])
emailDf.to_csv("emails.csv",index=False)
parsed_data_list = []

for index, row in emailDf.iterrows():
    obj=features.Features()
    obj.message_id=regerParser.extract_message_id(row['message'])
    obj.sender_email = regerParser.extract_sender_email(row['message']) 
    obj.reciever_email = regerParser.extract_reciever_email(row['message']) 
    obj.sender_org = regerParser.extract_sender_org(row['message']) 
    obj.reciever_org = regerParser.extract_reciever_org(row['message']) 
    obj.body = regerParser.extract_body(row['message']) 
    obj.date = regerParser.extract_date(row['message']) 
    parsed_data_list.append(obj)
    print(str(obj))

