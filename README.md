# Twitter listener geoparsing integration

## requirements
### python packages
- mordecai (`pip install mordecai`)
- spacy english model (`python -m spacy download en_core_web_lg`)

### elasticsearch docker
- set up 
```
    docker pull elasticsearch:5.5.2
    wget https://s3.amazonaws.com/ahalterman-geo/geonames_index.tar.gz --output-file=wget_log.txt
    tar -xzf geonames_index.tar.gz
```
- from directory containing `geonames_index`
`docker run -d -p 127.0.0.1:9200:9200 -v $(pwd)/geonames_index/:/usr/share/elasticsearch/data elasticsearch:5.5.2`

## on_data logic
```python
# init class
from geotagger import VCGeotagger
tagger = VCGeotagger()

# in on_data
city, state = "None", "None"
if dat["place"]:
    city, state = tagger.placetag(dat["place"]["full_name"])
if city == "None" and state == "None":
    city, state = tagger.geotag(location)
```
