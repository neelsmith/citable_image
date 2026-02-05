# Retrieving binary image data

You  can use the `citable_image` library to retrieve binary image data from an IIIF image server that understands site URN citation.


## Instantiate a service


```python
import citable_image as ci
baseurl = "http://www.homermultitext.org/iipsrv"
root = "/project/homer/pyramidal/deepzoom"
service = ci.IIIFService(baseurl=baseurl, pathroot=root)
```


should be written... (code, not docs!)

## Compose a request

- I *think* this code is written...


```python
img = Cite2Urn.from_string("urn:cite2:citebne:complutensian.v1:v1p19@0.6858,0.06753,0.1013,0.02509")
```

iifrequest = url(img, service)


