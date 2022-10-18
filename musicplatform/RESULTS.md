## create some artists

```python
from artists.models import Artist
Artist.objects.create(stage_name="Imagine Dragons",social_link="https://www.imaginedragonsmusic.com/")
```

<Artist: Imagine Dragons>

```python
Artist.objects.create(stage_name="Avicii",social_link="https://avicii.com/")
```

<Artist: Avicii>

```python
Artist.objects.create(stage_name="Adele",social_link="https://www.adele.com/")
```

<Artist: Adele>

## list down all artists

```python
Artist.objects.all()
```

<QuerySet [<Artist: Adele>, <Artist: Avicii>, <Artist: Imagine Dragons>]>

## list down all artists sorted by name

```python
Artist.objects.order_by('stage_name')
```

<QuerySet [<Artist: Adele>, <Artist: Avicii>, <Artist: Imagine Dragons>]>

## list down all artists whose name starts with a

```python
Artist.objects.filter(stage_name__istartswith='a')
```

<QuerySet [<Artist: Adele>, <Artist: Avicii>]>

## in 2 different ways, create some albums and assign them to any artists (hint: use objects manager and use the related object reference)

```python
from albums.models import Album
import datetime
from django.utils import timezone
imagine_dragons = Artist.objects.get(stage_name__iexact='imagine dragons')
imagine_dragons.album_set.create(name='Evolve',
                                 creation_datetime=timezone.now(),
                                 release_datetime=datetime.datetime(2017, 6, 23),
                                 cost=9.49)
```

RuntimeWarning: DateTimeField Album.release_datetime received a naive datetime (2017-06-23 00:00:00) while time zone support is active.
warnings.warn(  
<Album: Evolve>

```python
Album.objects.create(name='Mercury - Acts 1 & 2',
                     creation_datetime=timezone.now(),
                     release_datetime=datetime.datetime(2022, 7, 1),
                     cost=19.99, artist=imagine_dragons.id)
```

RuntimeWarning: DateTimeField Album.release_datetime received a naive datetime (2022-07-01 00:00:00) while time zone support is active.
warnings.warn(  
<Album: Mercury - Acts 1 & 2>

## get the latest released album

```python
Album.objects.order_by('-release_datetime')[0]
```

<Album: Mercury - Acts 1 & 2>

## get all albums released before today

```python
Album.objects.filter(release_datetime__lt=datetime.date.today())
```

RuntimeWarning: DateTimeField Album.release_datetime received a naive datetime (2022-10-18 00:00:00) while time zone support is active.
warnings.warn(  
<QuerySet [<Album: Evolve>, <Album: Mercury - Acts 1 & 2>]>

## get all albums released today or before but not after today

```python
Album.objects.filter(release_datetime__lte=datetime.date.today())
```

RuntimeWarning: DateTimeField Album.release_datetime received a naive datetime (2022-10-18 00:00:00) while time zone support is active.
warnings.warn(  
<QuerySet [<Album: Evolve>, <Album: Mercury - Acts 1 & 2>]>

## count the total number of albums (hint: count in an optimized manner)

```python
Album.objects.all().count()
```

2

## in 2 different ways, for each artist, list down all of his/her albums (hint: use objects manager and use the related object reference)

```python
for artist in Artist.objects.all():
    print(artist)
    print(Album.objects.filter(artist=artist))
```

Adele
<QuerySet []>
Avicii
<QuerySet []>
Imagine Dragons
<QuerySet [<Album: Evolve>, <Album: Mercury - Acts 1 & 2>]>

```python
for artist in Artist.objects.all():
    print(artist)
    print(artist.album_set.all())
```

Adele
<QuerySet []>
Avicii
<QuerySet []>
Imagine Dragons
<QuerySet [<Album: Evolve>, <Album: Mercury - Acts 1 & 2>]>

## list down all albums ordered by cost then by name (cost has the higher priority)

```python
Album.objects.order_by('cost', 'name')
```

<QuerySet [<Album: Evolve>, <Album: Mercury - Acts 1 & 2>]>
