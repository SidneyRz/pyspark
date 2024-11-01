# -*- coding: utf-8 -*-
"""Tarea.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1yNECFcX_wTqELfVUROIQdfQ3kc2Fb5Kc
"""

from pyspark import SparkContext

"""# **distinct**"""
"""Elimina los valores duplicados para que solo haya valores únicos."""

sc = SparkContext.getOrCreate()

rdd = sc.parallelize([1, 2, 2, 3, 4, 5, 5, 6, 7])

distinct_rdd = rdd.distinct()

print(distinct_rdd.collect())

"""# **groupByKey**"""
"""Agrupa todos los valores que tienen la misma clave."""

rdd = sc.parallelize([('a', 1), ('b', 2), ('a', 3), ('b', 4), ('c', 5), ('b', 6), ('c', 7)])

grouped_rdd = rdd.groupByKey()

print([(k, list(v)) for k, v in grouped_rdd.collect()])

"""# **reduceBuKey**"""
"""Suma todos los valores que tengan la misma clave."""

rdd = sc.parallelize([('a', 1), ('b', 2), ('a', 3), ('b', 4), ('c', 5), ('b', 6), ('c', 7)])

reduced_rdd = rdd.reduceByKey(lambda a, b: a + b)

print(reduced_rdd.collect())

"""# **sortByKey**"""
"""Ordena los pares en función de la clave."""

rdd = sc.parallelize([(3, 'a'), (1, 'b'), (2, 'c'), (4, 'd'), (5, 'e'), (6, 'f'), (7, 'g')])

sorted_rdd = rdd.sortByKey()

print(sorted_rdd.collect())

"""# **join**"""
"""Une los dos RDDs por clave, generando un nuevo RDD con pares clave, generando un nuevo RDD con pares clave y tuplas de los valores asociados."""

rdd1 = sc.parallelize([('a', 1), ('b', 2), ('c', 3)])

rdd2 = sc.parallelize([('a', 4), ('b', 5), ('b', 8), ('c', 7), ('d', 6)])

joined_rdd = rdd1.join(rdd2)

print(joined_rdd.collect())
