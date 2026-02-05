# Retrieving binary image data

You  can use the `citable_image` library to retrieve binary image data from an IIIF image server that understands site URN citation.


## Instantiate a service


```python
import citable_image as ci
baseurl = "http://www.homermultitext.org/iipsrv"
root = "/project/homer/pyramidal/deepzoom"
service = ci.IIIFService(baseurl=baseurl, pathroot=root)
```


## Identify an image by URN


```python
from urn_citation import Cite2Urn

imgurn = Cite2Urn.from_string("urn:cite2:citebne:complutensian.v1:v1p19@0.6858,0.06753,0.1013,0.02509")
```


## Compose and send IIIF requests.

Compose a IIIF request URL with the `iiif_url` function:

```python
iifrequest = ci.iiif_url(imgurn, service)
```


An image from an IIIF service with the `iiif_image` function:d


```python
img = ci.iiif_image(imgurn, service)
```


