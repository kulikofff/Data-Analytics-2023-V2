# Installed here - C:\Windows\System32\y
# Tutorial here - https://www.pyxll.com/docs/videos/worksheet-functions.html
# Installation and some guide https://youtu.be/vyDd_3r93cU


from pyxll import xl_func


@xl_func()
def ml_excel_predict(f1,f2,f3,f4):
    
    """Enter 4 values of any format.

    Returns:
        array: classification type = 0 or 1
    """
    
    import xgboost as xgb
    import pandas as pd
    
    clf = xgb.XGBClassifier()
    
    
    # Load data for concatination. Why? Because using enable_categorical=True in xgboost, I suppose. When I predict biп amount data (from evaluation dataset,
    # I receive good result. But if I predict only one value - I receive not correct reгде (always 1 or 0). After some exepiremts I tried to put more data in 
    # prediction - and it wokrs well. May be it happens , because enable_categorical=True is experimental. Or because of my hands:)) In russian it is called - 
    # "Костыль" :)
    
    traindata = pd.read_csv("E:\KULIKOV\ML\MLCourseAI\MLCourseAI\MLinExcel\Male_Female.csv")
    traindata = traindata.drop(['Gender'], axis = 1)
    traindata["Favorite Color"] = traindata["Favorite Color"].astype("category")
    traindata["Favorite Music Genre"] = traindata["Favorite Music Genre"].astype("category")
    traindata["Favorite Beverage"] = traindata["Favorite Beverage"].astype("category")
    traindata["Favorite Soft Drink"] = traindata["Favorite Soft Drink"].astype("category")
   
        
    # Load my data     
    testdata = pd.DataFrame({"Favorite Color": [f1], "Favorite Music Genre": [f2], "Favorite Beverage": [f3], "Favorite Soft Drink": [f4]})  
    testdata["Favorite Color"] = testdata["Favorite Color"].astype("category")
    testdata["Favorite Music Genre"] = testdata["Favorite Music Genre"].astype("category")
    testdata["Favorite Beverage"] = testdata["Favorite Beverage"].astype("category")
    testdata["Favorite Soft Drink"] = testdata["Favorite Soft Drink"].astype("category")
    
    
    t0 = pd.DataFrame()
    t0 = pd.concat([traindata, testdata], ignore_index=True)
    t0["Favorite Color"] = t0["Favorite Color"].astype("category")
    t0["Favorite Music Genre"] = t0["Favorite Music Genre"].astype("category")
    t0["Favorite Beverage"] = t0["Favorite Beverage"].astype("category")
    t0["Favorite Soft Drink"] = t0["Favorite Soft Drink"].astype("category")

    print(testdata)
    print()
    print(t0)
    
    clf.load_model("E:\KULIKOV\ML\MLCourseAI\MLCourseAI\MLinExcel\Male_Female_Model.json")
    prediction_all = clf.predict(t0)
    print(prediction_all)
    prediction_my = prediction_all[-1]

    return prediction_my


if __name__ == "__main__":
#    print(ml_excel_predict("Cool","Electronic","Doesn't drink","Fanta"))  # must be 0 or 1
#        print(ml_excel_predict('Warm','Rock','Wine','Coca Cola/Pepsi'))  # must be 0 (Female)
        print(ml_excel_predict('Warm','R&B and soul','Wine','Other'))  # must be 1 (Male)