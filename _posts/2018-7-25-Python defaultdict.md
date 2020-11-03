---
layout: post
title: Python - Custom defaultdict (ENG)
description: Show you a way how to implement general custom class with defaultdict which you can nested together to create very useful structures.
author: Petr Lorenc
comments: true
tag: machine learning
---

I want to show you a way how to implement general custom class with defaultdict which you can nested together to create very useful structures.

<h2> Task </h2>

  * Make a counter which will store a number of a certain event for certain time window
  * After specified amount of time will save the values of a counter into the database (not on this pages)
  * The event is described by **datetime** (of logging window), **id, zone_id and type** 

Firstly, I was thinking about series of nested defaultdict:

```python
self._counter = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: defaultdict(int))))
...
self._counter[datetime][item_id][zone_id][type] += count
```
 
That solution is working but is there a "better more object-oriented" way? Of course - more complicated custom class with defaultdict as a parameter:

```python
class BaseCounter(object): 
  def __init__(self):
    print ("BaseCounter init = ")
    self._counter = 0

  def increment(self, count=1):       
    self._counter += count

  def items(self):
    return self._counter


class DictCounter(object):
  def __init__(self, dict_class):
    self._counter = defaultdict(dict_class)

  def increment(self, key, value, *args, **kwargs):
    print (key, value, args, kwargs)
    self._counter[key].increment(value, *args, **kwargs)

  def items(self):
    result = []
    for key, counter in self._counter.items():
        result.append((key, counter.items()))
    return result
```

Then if you want to do the same as above:

```python
y = DictCounter(lambda: DictCounter(lambda: DictCounter(lambda: BaseCounter())))

y.increment(10,1,2,3)
y.increment(10,1,2,3)
y.increment(10,1,3,3)
y.increment(10,2,2,3)
```

to get:

```python
10 1 2 6
10 1 3 3
10 2 2 3
```

<h2> Granularity </h2>

Nice way ... but what about time granularity (time logging window)? Granularity means that I want to group events in certain time window (for example 5 minutes). So, we can just make a child of class **DictCounter** with that functionality:

```python
class TimeGranularCounter(DictCounter):
    def __init__(self, dict_class, granularity=10):
        super(TimeGranularCounter, self).__init__(dict_class)
        self._granularity = granularity

    def increment(self, item_id, zone_id, type, dt, count=1):  # pylint: disable=arguments-differ
        key = self.granular_datetime(dt)
        print(key)
        self._counter[key].increment(item_id, zone_id, type, count)

    def items(self):
        result = []
        for dt, counter in self._counter.items():
            for k, v in counter.items():
                result.append((dt, k, v))
        return result

    def granular_datetime(self, dt):
        assert isinstance(dt, datetime)
        minute = dt.minute - (dt.minute % self._granularity)
        return dt.replace(minute=minute, second=0, microsecond=0) + timedelta(minutes=self._granularity)
```

usage is as simple as DictCounter:

```python
counter = TimeGranularCounter(DictCounter(DictCounter(DictCounter(BaseCounter))), 12)

dt = datetime(2018, 7, 25, 10, 48)
counter.increment(327, 874, 'click', dt, 11)
counter.increment(327, 874, 'click', dt, 11)

dt = datetime(2018, 7, 25, 10, 50)
counter.increment(327, 874, 'click', dt, 11)

dt = datetime(2018, 7, 25, 23, 48)
counter.increment(327, 874, 'click', dt, 11)
counter.increment(327, 874, 'impress', dt, 11)
```

to get 
```python
2018-07-25 11:00:00 327 [(874, [('click', 33)])]
2018-07-26 00:00:00 327 [(874, [('click', 11), ('impress', 11)])]
```

Pretty nice, hah?

<h2> Watch my mistake </h2>

Don't do the same mistake as me ... If you define DictCounter like this

```python
class DictCounter(object):
  def __init__(self, dict_class):
    self._counter = defaultdict(lambda: dict_class)
    ...

y = DictCounter(DictCounter(DictCounter(BaseCounter())))
```

it won't be working. Try to guess why not?

<h3> Explanation </h3>

Because that way, we will be using the same object for every new key in our object's counter. That means that there will be unexpected behavior with references. For more detail see <a href="https://stackoverflow.com/questions/51522943/python-custom-class-to-work-with-nested-defaultdict?noredirect=1#comment90019386_51522943">this</a>.




























