# AI_Educational
Jupyter Notebooks and datasets for AI educational purposes

This repository contains AI material used for the books and courses I author and co-author.

Everything is opensource to be shared and used by all.

Google Colaboratory Jupyter Notebooks are self-contained.

# images citations:
cat.jpg: Denis Rothman<br>
butterfly: [Wikicommons](https://commons.wikimedia.org/wiki/File:Small_heath_(Coenonympha_pamphilus)_P.jpg)<br>
cup:[Wikicommons](https://commons.wikimedia.org/wiki/File:A_small_cup_of_coffee.JPGe)<br>
bird:[Wikicommons](https://commons.wikimedia.org/wiki/File:Small_minivet_(Pericrocotus_cinnamomeus_pallidus)_male_Narlai.jpg)<br>
boat:[Wikicommons]https://commons.wikimedia.org/wiki/File:Small_sport_fishing_boat.jpg)


## Opening Google Jupytyer Notebooks online
There is nothing to download or install locally unless you wish to do so.

You can access Google Colaboratory by clicking on one of the Jupyter Notebooks in any of the repositories in the Denis2054 repositories on GitHub. Then click the Colab button at the top of the Notebook.

You can also download the Jupyter Notebook and open it from Colaboratory:
[Link to Colaboratory](https://colab.research.google.com/)

### Before running a Jupyter Notebook when using it online with Google Drive, save it directly in your drive using the Colaboratory Menu.

## Accessing external data

You can choose to download the data and adapt the code to your directory paths. 
You can also run the datasets online.

Once the Notebook has been opened, you can view the code as well as the last results calculated.
You can also run itself. 
To do so, for applications that require external data, in most cases, you will have to download the data in this repository contained in the directory named "datasets". Then upload the data to any online repository that runs with Google Colaboratory.

The examples in the Juypter Notebooks in Denis2054 repositories generally contain datasets that are stored in Google Drive.
In this case the code must contain:

```ruby
from google.colab import drive
```

For more:
[Link to External data documentation](https://colab.research.google.com/notebooks/io.ipynb)



## Using Google Drive

Once you have added the right library header, then for Denis2054 Jupyter Notebook data, you can use  the same basic path as shown in following example:

```ruby
json_file = open('/content/gdrive/My Drive/datasets/chapter12/dataset/model/model.json', 'r')
```
In this path, your Google drive root directory will be 

```ruby
'/content/gdrive/My Drive/datasets/...)'
```

Then for each program you can add a subdirectory to that path:

```ruby
'/content/gdrive/My Drive/datasets/[a program's subdirectory/]', 'r')
```
The advantage of following this specific path structure, is that once you can load the directories in your Google Drive as strutured in the code of the Jupyter Notebooks in Denis2054 repositories without have to change the code.

**Note:** Download the 'datasets' directory from this repository and then upload in your drive following the path indicated in the program. Or you can change the path in the program if you wish to use another path.

## Try an example: an Edge Detection Python program

The Edge Detection example, https://github.com/Denis2054/NEXTGENAI/blob/master/Edge_detection_V3.ipynb, is just to show that you won't need to install, download or configure anything to use these notebooks<br>


