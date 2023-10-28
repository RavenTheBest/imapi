## Version 1.0.0

**Release Date:** October 28, 2023

### Functions

* Added linklist() function to return a list of all images by searches

```python
list = imapi.linklist("cats")
print(list)
```
output will be a list of cats image links.
* Added single() function to return a single image link by searches

```python
image_link = imapi.single("cats")
print(image_link)
```
output will be a single link of cats image.

* added download() function which save the image file on user device

```python
save = imapi.download("cats","jpg")
print(save)
```

output will be cats.jpg and save it as cats.jpg


### Bug fixed

* No internet message, function, will return an "error occured" when error happened
* Minor issue
