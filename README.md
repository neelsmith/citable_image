# `citable_corpus`

Work with a corpus of texts canonically citable by CtsUrn.


## TBD

Julia to imitate:

```julia
using CitableImage
baseurl = "http://www.homermultitext.org/iipsrv"
root = "/project/homer/pyramidal/deepzoom"
service = IIIFservice(baseurl, root)

using CitableObject
img = Cite2Urn("urn:cite2:hmt:vaimg.2017a:VA012RN_0013")

iifrequest = url(img, service)

```

## In web pages

```julia
using CitableObject
img = Cite2Urn("urn:cite2:hmt:vaimg.2017a:VA012RN_0013")

mdembed = markdownImage(img, service; w = 200)

ict = "http://www.homermultitext.org/ict2/?"
embedwlink = linkedMarkdownImage(ict, img, service; w=100, caption="folio 12 recto")

htmlimg = htmlImage(img, service; w = 200)


```