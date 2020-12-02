from KLS_EDA import new_kls_df
from sklearn.model_selection import train_test_split

# Splitting the data into training data and test data

X = new_kls_df[1:4].to_numpy().reshape(new_kls_df[1:4].size//3, 3)
y = new_kls_df.loc['Karachi Electric'].to_numpy().reshape(-1)
others_blamed_train, others_blamed_test, ke_train, ke_test = train_test_split(X, y, test_size = 0.3, random_state = 1, stratify = y)