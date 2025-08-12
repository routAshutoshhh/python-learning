import seaborn as sns
import pickle

print(sns.get_dataset_names())
dataset = sns.load_dataset('penguins')

#we  have got the dataset 
print(dataset.head())


#creating  the file with the pickle with  a name 
filename = 'file.pkl'

#now we will dump the dataset into the file 
#serialising the files
pickle.dump(dataset ,open(filename , 'wb'))


#deserialising the files
loaded_dataset  = pickle.load(open(filename , 'rb'))