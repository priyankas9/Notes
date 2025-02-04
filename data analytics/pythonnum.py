{"cells":[{"cell_type":"markdown","metadata":{"id":"s1d42PrEdOm9"},"source":["# Numerical Computing with Python and Numpy\n","\n","![]
(https://i.imgur.com/mg8O3kd.png)\n","\n","This tutorial series is a beginner-friendly introduction to programming and data analysis using the
Python programming language. These tutorials take a practical and coding-focused approach. The best way to learn the material is to execute
the code and experiment with it yourself."]},{"cell_type":"markdown","metadata":{"id":"hOrmb_6odOnC"},"source":["This tutorial covers the
following topics:\n","\n","- Working with numerical data in Python\n","- Going from Python lists to Numpy arrays\n","- Multi-dimensional Numpy
arrays and their benefits\n","- Array operations, broadcasting, indexing, and slicing\n","- Working with CSV data files using Numpy"]},
{"cell_type":"markdown","metadata":{"id":"7QrrV5ZgdOnC"},"source":["## Working with numerical data\n","\n","The \"data\" in *Data Analysis*
typically refers to numerical data, e.g., stock prices, sales figures, sensor measurements, sports scores, database tables, etc. The [Numpy]
(https://numpy.org) library provides specialized data structures, functions, and other tools for numerical computing in Python. Let's work through
an example to see why & how to use Numpy for working with numerical data.\n","\n","\n","> Suppose we want to use climate data like the
temperature, rainfall, and humidity to determine if a region is well suited for growing apples. A simple approach for doing this would be to
formulate the relationship between the annual yield of apples (tons per hectare) and the climatic conditions like the average temperature (in
degrees Fahrenheit), rainfall (in millimeters) & average relative humidity (in percentage) as a linear equation.\n",">\n","> `yield_of_apples = w1 *
temperature + w2 * rainfall + w3 * humidity`\n","\n","We're expressing the yield of apples as a weighted sum of the temperature, rainfall, and
humidity. This equation is an approximation since the actual relationship may not necessarily be linear, and there may be other factors involved.
But a simple linear model like this often works well in practice.\n","\n","Based on some statical analysis of historical data, we might come up with
reasonable values for the weights `w1`, `w2`, and `w3`. Here's an example set of values:"]},{"cell_type":"code","execution_count":null,"metadata":
{"id":"RH_pLthYdOnD"},"outputs":[],"source":["w1, w2, w3 = 0.3, 0.2, 0.5"]},{"cell_type":"markdown","metadata":{"id":"roJsOc66dOnE"},"source":
["Given some climate data for a region, we can now predict the yield of apples. Here's some sample data:\n","\n"," \n","\n","To begin, we can
define some variables to record climate data for a region."]},{"cell_type":"code","execution_count":null,"metadata":{"id":"-
N1Op198dOnF"},"outputs":[],"source":["kanto_temp = 73\n","kanto_rainfall = 67\n","kanto_humidity = 43"]},{"cell_type":"markdown","metadata":
{"id":"imMOaTJJdOnF"},"source":["We can now substitute these variables into the linear equation to predict the yield of apples."]},
{"cell_type":"code","execution_count":null,"metadata":{"id":"jguWJvaWdOnG","outputId":"43bc73ec-7592-42e8-c0f5-4b9e985c7fb5"},"outputs":
[{"data":{"text/plain":["56.8"]},"execution_count":3,"metadata":{},"output_type":"execute_result"}],"source":["kanto_yield_apples = kanto_temp * w1
+ kanto_rainfall * w2 + kanto_humidity * w3\n","kanto_yield_apples"]},{"cell_type":"code","execution_count":null,"metadata":
{"id":"R4iOT9xCdOnH","outputId":"cb79ba96-40b6-4241-8110-d93eee0fc7c6"},"outputs":[{"name":"stdout","output_type":"stream","text":["The
expected yield of apples in Kanto region is 56.8 tons per hectare.\n"]}],"source":["print(\"The expected yield of apples in Kanto region is {} tons per
hectare.\".format(kanto_yield_apples))"]},{"cell_type":"markdown","metadata":{"id":"_ui5OE5_dOnI"},"source":["To make it slightly easier to
perform the above computation for multiple regions, we can represent the climate data for each region as a vector, i.e., a list of numbers."]},
{"cell_type":"code","execution_count":null,"metadata":{"id":"IwZb-WLidOnI"},"outputs":[],"source":["kanto = [73, 67, 43]\n","johto = [91, 88,
64]\n","hoenn = [87, 134, 58]\n","sinnoh = [102, 43, 37]\n","unova = [69, 96, 70]"]},{"cell_type":"markdown","metadata":
{"id":"EGTmdZrvdOnI"},"source":["The three numbers in each vector represent the temperature, rainfall, and humidity data,
respectively.\n","\n","We can also represent the set of weights used in the formula as a vector."]},
{"cell_type":"code","execution_count":null,"metadata":{"id":"8kKvXPBddOnJ"},"outputs":[],"source":["weights = [w1, w2, w3]"]},
{"cell_type":"code","source":["list(enumerate(weights))"],"metadata":{"colab":
{"base_uri":"https://localhost:8080/"},"id":"6ESmw64vU3tb","executionInfo":
{"status":"ok","timestamp":1710811773520,"user_tz":-345,"elapsed":9,"user":{"displayName":"Abhishek
Paudel","userId":"15094254969844955559"}},"outputId":"10cd6c86-28ce-47cb-a362-da3424712ae1"},"execution_count":null,"outputs":
[{"output_type":"execute_result","data":{"text/plain":["[(0, 0.3), (1, 0.2), (2, 0.5)]"]},"metadata":{},"execution_count":8}]},{"cell_type":"code","source":
["for x,y in enumerate(weights):\n"," print(f'The {x}th element is {y}')"],"metadata":{"colab":
{"base_uri":"https://localhost:8080/"},"id":"cxEpZuyWVFpt","executionInfo":
{"status":"ok","timestamp":1710811848411,"user_tz":-345,"elapsed":697,"user":{"displayName":"Abhishek
Paudel","userId":"15094254969844955559"}},"outputId":"824a99ce-99f9-43ef-9dde-5bdc67b21d78"},"execution_count":null,"outputs":
[{"output_type":"stream","name":"stdout","text":["The 0th element is 0.3\n","The 1th element is 0.2\n","The 2th element is 0.5\n"]}]},
{"cell_type":"markdown","metadata":{"id":"fpSBaNKEdOnJ"},"source":["We can now write a function `crop_yield` to calcuate the yield of apples (or
any other crop) given the climate data and the respective weights."]},{"cell_type":"code","execution_count":null,"metadata":
{"id":"xjSZni0VdOnJ","outputId":"d25f7c55-4351-4440-e17e-15d7c401c29a","colab":{"base_uri":"https://localhost:8080/"},"executionInfo":
{"status":"ok","timestamp":1710811672794,"user_tz":-345,"elapsed":441,"user":{"displayName":"Abhishek
Paudel","userId":"15094254969844955559"}}},"outputs":[{"output_type":"execute_result","data":{"text/plain":["[(73, 0.3), (67, 0.2), (43,
0.5)]"]},"metadata":{},"execution_count":6}],"source":["list(zip(kanto, weights))"]},{"cell_type":"code","execution_count":null,"metadata":
{"id":"KtytdoFqdOnJ","colab":{"base_uri":"https://localhost:8080/","height":110},"executionInfo":
{"status":"error","timestamp":1710811675970,"user_tz":-345,"elapsed":6,"user":{"displayName":"Abhishek
Paudel","userId":"15094254969844955559"}},"outputId":"7561373e-8821-4663-eadb-b360d9383490"},"outputs":
[{"output_type":"error","ename":"SyntaxError","evalue":"incomplete input (, line 1)","traceback":["\u001b[0;36m File \u001b[0;32m\"\"\u001b[0;36m,
line \u001b[0;32m1\u001b[0m\n\u001b[0;31m def crop_yield(region, weights):\u001b[0m\n\u001b[0m
^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m incomplete input\n"]}],"source":["def crop_yield(region, weights):\n","
result = 0\n"," for x, w in zip(region, weights):\n"," result += x * w\n"," return result"]},{"cell_type":"code","execution_count":null,"metadata":
{"id":"TKi8KvNxdOnJ","outputId":"d66e3b7d-cd7e-4e70-b9f3-028cb15815ba"},"outputs":[{"data":{"text/plain":
["56.8"]},"execution_count":6,"metadata":{},"output_type":"execute_result"}],"source":["crop_yield(kanto, weights)"]},
{"cell_type":"code","execution_count":null,"metadata":{"id":"AaePCBwsdOnK","outputId":"cc6a75bf-b835-4188-995e-4fc43f3e7b38"},"outputs":
[{"data":{"text/plain":["76.9"]},"execution_count":7,"metadata":{},"output_type":"execute_result"}],"source":["crop_yield(johto, weights)"]},
{"cell_type":"code","execution_count":null,"metadata":{"id":"34GBlGuNdOnK","outputId":"f94fe364-f613-401b-e61a-c2d365aa9a77"},"outputs":
[{"data":{"text/plain":["74.9"]},"execution_count":8,"metadata":{},"output_type":"execute_result"}],"source":["crop_yield(unova, weights)"]},
{"cell_type":"markdown","metadata":{"id":"yGYy1QARdOnK"},"source":["## Going from Python lists to Numpy arrays\n","\n","\n","The calculation
performed by the `crop_yield` (element-wise multiplication of two vectors and taking a sum of the results) is also called the *dot product*. Learn
more about dot product here: https://www.khanacademy.org/math/linear-algebra/vectors-and-spaces/dot-cross-products/v/vector-dot-productand-vector-length .\n","\n","The Numpy library provides a built-in function to compute the dot product of two vectors. However, we must first
convert the lists into Numpy arrays.\n","\n","Let's install the Numpy library using the `pip` package manager."]},
{"cell_type":"code","execution_count":null,"metadata":{"id":"dtOJXsVjdOnK","outputId":"e40c908e-2b4e-496c-e743-293803959739"},"outputs":
[{"name":"stderr","output_type":"stream","text":["\n","[notice] A new release of pip available: 22.3.1 -> 23.0\n","[notice] To update, run: python.exe -
m pip install --upgrade pip\n"]}],"source":["!pip install numpy --upgrade --quiet"]},{"cell_type":"markdown","metadata":
{"id":"boH9QK3CdOnL"},"source":["Next, let's import the `numpy` module. It's common practice to import numpy with the alias `np`."]},
{"cell_type":"code","execution_count":null,"metadata":{"id":"4chMvqBWdOnL"},"outputs":[],"source":["import numpy as np\n","import pandas as
pd"]},{"cell_type":"markdown","metadata":{"id":"tiTClgpAdOnL"},"source":["We can now use the `np.array` function to create Numpy arrays."]},
{"cell_type":"code","execution_count":null,"metadata":{"id":"_6oLdsKKdOnL"},"outputs":[],"source":["kanto = np.array([73, 67, 43])"]},
{"cell_type":"code","execution_count":null,"metadata":{"id":"zHKuxmz3dOnL","outputId":"0c482c4c-9c5c-4cdc-d108-6807857f5945","colab":
{"base_uri":"https://localhost:8080/"},"executionInfo":{"status":"ok","timestamp":1710811979844,"user_tz":-345,"elapsed":4,"user":
{"displayName":"Abhishek Paudel","userId":"15094254969844955559"}}},"outputs":[{"output_type":"execute_result","data":{"text/plain":["array([73,
67, 43])"]},"metadata":{},"execution_count":14}],"source":["kanto"]},{"cell_type":"code","execution_count":null,"metadata":
{"id":"nNXY8Z31dOnL","outputId":"b2afe92b-5808-43cb-de65-074ce653ed76","colab":{"base_uri":"https://localhost:8080/"},"executionInfo":
{"status":"ok","timestamp":1710811983624,"user_tz":-345,"elapsed":3,"user":{"displayName":"Abhishek
Paudel","userId":"15094254969844955559"}}},"outputs":[{"output_type":"execute_result","data":{"text/plain":["numpy.ndarray"]},"metadata":
{},"execution_count":15}],"source":["type(kanto)"]},{"cell_type":"code","execution_count":null,"metadata":{"id":"UYahd1wddOnL"},"outputs":
[],"source":["weights = np.array([w1, w2, w3])\n","# we can write like below as well.\n","# weights = np.array(weights)"]},
{"cell_type":"code","execution_count":null,"metadata":{"id":"NA6AXknvdOnM","outputId":"98154df4-10e3-4349-ee85-9e02bd084db6"},"outputs":
[{"data":{"text/plain":["array([0.3, 0.2, 0.5])"]},"execution_count":15,"metadata":{},"output_type":"execute_result"}],"source":["weights"]},
{"cell_type":"markdown","metadata":{"id":"l4FUesOxdOnM"},"source":["Numpy arrays have the type `ndarray`."]},
{"cell_type":"code","execution_count":null,"metadata":{"id":"L6_WLJwGdOnM","outputId":"bc6cf4f6-1ff3-44c4-9b86-64511db1bb56"},"outputs":
[{"data":{"text/plain":["numpy.ndarray"]},"execution_count":16,"metadata":{},"output_type":"execute_result"}],"source":["type(kanto)"]},
{"cell_type":"code","execution_count":null,"metadata":{"id":"Z1--KaJkdOnM","outputId":"a2824b71-d0b9-449b-a6d7-0e95b504ca52"},"outputs":
[{"data":{"text/plain":["numpy.ndarray"]},"execution_count":17,"metadata":{},"output_type":"execute_result"}],"source":["type(weights)"]},
{"cell_type":"markdown","metadata":{"id":"8mk4W4T6dOnM"},"source":["Just like lists, Numpy arrays support the indexing notation `[]`."]},
{"cell_type":"code","execution_count":null,"metadata":{"id":"jTQHDJiZdOnM","outputId":"aa83c982-2ad4-4c40-e990-d61b09157f06"},"outputs":
[{"data":{"text/plain":["0.3"]},"execution_count":18,"metadata":{},"output_type":"execute_result"}],"source":["weights[0]"]},
{"cell_type":"code","execution_count":null,"metadata":{"id":"hmvOjl0idOnN","outputId":"a75a20b3-2e6f-45d1-a669-674834ed07e0"},"outputs":
[{"data":{"text/plain":["43"]},"execution_count":19,"metadata":{},"output_type":"execute_result"}],"source":["kanto[2]"]},
{"cell_type":"markdown","metadata":{"id":"j2QN_lhUdOnN"},"source":["## Operating on Numpy arrays\n","\n","We can now compute the dot
product of the two vectors using the `np.dot` function."]},{"cell_type":"code","execution_count":null,"metadata":
{"id":"9boWG6kndOnN","outputId":"c4302f9d-cc1e-43fc-bea9-36e9a1c123d5"},"outputs":[{"data":{"text/plain":
["56.8"]},"execution_count":20,"metadata":{},"output_type":"execute_result"}],"source":["np.dot(kanto, weights)"]},
{"cell_type":"markdown","metadata":{"id":"js1vD1wMdOnN"},"source":["We can achieve the same result with low-level operations supported by
Numpy arrays: performing an element-wise multiplication and calculating the resulting numbers' sum."]},
{"cell_type":"code","execution_count":null,"metadata":{"id":"vqLiXLpNdOnN"},"outputs":[],"source":["(kanto * weights).sum()"]},
{"cell_type":"markdown","metadata":{"id":"aqIkPAK6dOnT"},"source":["The `*` operator performs an element-wise multiplication of two arrays if
they have the same size. The `sum` method calculates the sum of numbers in an array."]},{"cell_type":"code","execution_count":null,"metadata":
{"id":"sflhXze0dOnT"},"outputs":[],"source":["arr1 = np.array([1, 2, 3])\n","arr2 = np.array([4, 5, 6])"]},
{"cell_type":"code","execution_count":null,"metadata":{"id":"1xzDS8NodOnT","outputId":"155ad4d2-d42c-4380-f19c-f7bfbc19b939"},"outputs":
[{"data":{"text/plain":["array([ 4, 10, 18])"]},"execution_count":22,"metadata":{},"output_type":"execute_result"}],"source":["arr1 * arr2"]},
{"cell_type":"code","execution_count":null,"metadata":{"id":"L0Ff8JAudOnV","outputId":"d081cb81-d975-410a-ffa7-e6af790c5a84"},"outputs":
[{"data":{"text/plain":["15"]},"execution_count":23,"metadata":{},"output_type":"execute_result"}],"source":["arr2.sum()"]},
{"cell_type":"markdown","metadata":{"id":"d_xqTENRdOnV"},"source":["## Benefits of using Numpy arrays\n","\n","Numpy arrays offer the
following benefits over Python lists for operating on numerical data:\n","\n","- **Ease of use**: You can write small, concise, and intuitive
mathematical expressions like `(kanto * weights).sum()` rather than using loops & custom functions like `crop_yield`.\n","- **Performance**:
Numpy operations and functions are implemented internally in C++, which makes them much faster than using Python statements & loops that
are interpreted at runtime\n","\n","Here's a comparison of dot products performed using Python loops vs. Numpy arrays on two vectors with a
million elements each."]},{"cell_type":"code","execution_count":null,"metadata":{"id":"cVJNgavNdOnV"},"outputs":[],"source":["# Python
lists\n","arr1 = list(range(1000000))\n","arr2 = list(range(1000000, 2000000))\n","\n","# Numpy arrays\n","arr1_np = np.array(arr1)\n","arr2_np =
np.array(arr2)"]},{"cell_type":"code","execution_count":null,"metadata":{"colab":
{"base_uri":"https://localhost:8080/"},"id":"qTCZbecTdOnW","executionInfo":
{"status":"ok","timestamp":1710465504214,"user_tz":-345,"elapsed":479,"user":{"displayName":"Abhishek
Paudel","userId":"15094254969844955559"}},"outputId":"5f9bab19-118a-47f6-bfcc-484c177fe47f"},"outputs":
[{"output_type":"stream","name":"stdout","text":["CPU times: user 211 ms, sys: 940 µs, total: 212 ms\n","Wall time: 212 ms\n"]},
{"output_type":"execute_result","data":{"text/plain":["833332333333500000"]},"metadata":{},"execution_count":4}],"source":["#Magic Functions in
Ipython (%%, @, .....)\n","%%time\n","result = 0\n","for x1, x2 in zip(arr1, arr2):\n"," result += x1*x2\n","result"]},
{"cell_type":"code","execution_count":null,"metadata":{"id":"WkZ3cgCedOnW","outputId":"d28f58bd-9d2a-468a-9790-34e61f0aa2bd"},"outputs":
[{"name":"stdout","output_type":"stream","text":["CPU times: total: 0 ns\n","Wall time: 1.51 ms\n"]},{"data":{"text/plain":
["-1942957984"]},"execution_count":26,"metadata":{},"output_type":"execute_result"}],"source":["%%time\n","result = np.dot(arr1_np,
arr2_np)\n","result"]},{"cell_type":"markdown","metadata":{"id":"zDRVNV83dOnW"},"source":["As you can see, using `np.dot` is 100 times faster
than using a `for` loop. This makes Numpy especially useful while working with really large datasets with tens of thousands or millions of data
points.\n","\n","Let's save our work before continuing."]},{"cell_type":"markdown","metadata":{"id":"Q9geDTZHdOnW"},"source":["## Multidimensional Numpy arrays\n","\n","We can now go one step further and represent the climate data for all the regions using a single 2-dimensional
Numpy array."]},{"cell_type":"code","execution_count":null,"metadata":{"id":"HkmIqL21dOnW"},"outputs":[],"source":["climate_data = np.array([[73,
67, 43],\n"," [91, 88, 64],\n"," [87, 134, 58],\n"," [102, 43, 37],\n"," [69, 96, 70]])"]},{"cell_type":"code","execution_count":null,"metadata":
{"id":"qLpMqypldOnX","outputId":"12623ad3-dfa6-4aa8-8ed4-6c9536fe75b2","colab":{"base_uri":"https://localhost:8080/"},"executionInfo":
{"status":"ok","timestamp":1710812511240,"user_tz":-345,"elapsed":460,"user":{"displayName":"Abhishek
Paudel","userId":"15094254969844955559"}}},"outputs":[{"output_type":"execute_result","data":{"text/plain":["array([[ 73, 67, 43],\n"," [ 91, 88,
64],\n"," [ 87, 134, 58],\n"," [102, 43, 37],\n"," [ 69, 96, 70]])"]},"metadata":{},"execution_count":18}],"source":["climate_data"]},
{"cell_type":"code","source":["type(climate_data)"],"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"7fCQFJUpX0xC","executionInfo":
{"status":"ok","timestamp":1710812528296,"user_tz":-345,"elapsed":2,"user":{"displayName":"Abhishek
Paudel","userId":"15094254969844955559"}},"outputId":"189400e3-b136-4a65-b0cc-efb25939fed3"},"execution_count":null,"outputs":
[{"output_type":"execute_result","data":{"text/plain":["numpy.ndarray"]},"metadata":{},"execution_count":19}]},{"cell_type":"markdown","metadata":
{"id":"rjVcHAAwdOnX"},"source":["If you've taken a linear algebra class in high school, you may recognize the above 2-d array as a matrix with
five rows and three columns. Each row represents one region, and the columns represent temperature, rainfall, and humidity,
respectively.\n","\n","Numpy arrays can have any number of dimensions and different lengths along each dimension. We can inspect the length
along each dimension using the `.shape` property of an array.\n","\n"," \n","\n"]},{"cell_type":"code","execution_count":null,"metadata":
{"id":"LajrZXPvdOnX","outputId":"a4bea473-1b0e-47ae-aef0-b374d8182682","colab":{"base_uri":"https://localhost:8080/"},"executionInfo":
{"status":"ok","timestamp":1710744916157,"user_tz":-345,"elapsed":717,"user":{"displayName":"Abhishek
Paudel","userId":"15094254969844955559"}}},"outputs":[{"output_type":"execute_result","data":{"text/plain":["(5, 3)"]},"metadata":
{},"execution_count":5}],"source":["# 2D array (matrix)\n","climate_data.shape"]},{"cell_type":"code","execution_count":null,"metadata":
{"id":"KA51eNW9dOnX","outputId":"b9e11b6f-6760-4491-a28d-914c0bec25ad","colab":{"base_uri":"https://localhost:8080/"},"executionInfo":
{"status":"ok","timestamp":1710744998022,"user_tz":-345,"elapsed":446,"user":{"displayName":"Abhishek
Paudel","userId":"15094254969844955559"}}},"outputs":[{"output_type":"execute_result","data":{"text/plain":["array([0.3, 0.2, 0.5])"]},"metadata":
{},"execution_count":10}],"source":["weights"]},{"cell_type":"code","execution_count":null,"metadata":{"id":"8IAX9KCEdOnX","outputId":"ea4739a1-
5c4c-4b32-8733-e8f25f297a30","colab":{"base_uri":"https://localhost:8080/"},"executionInfo":
{"status":"ok","timestamp":1710745004917,"user_tz":-345,"elapsed":428,"user":{"displayName":"Abhishek
Paudel","userId":"15094254969844955559"}}},"outputs":[{"output_type":"execute_result","data":{"text/plain":["(3,)"]},"metadata":
{},"execution_count":11}],"source":["# 1D array (vector)\n","weights.shape"]},{"cell_type":"code","execution_count":null,"metadata":
{"id":"REQSLj4cdOnY"},"outputs":[],"source":["# 3D array\n","arr3 = np.array([\n"," [[11, 12, 13],\n"," [13, 14, 15]],\n"," [[15, 16, 17],\n"," [17, 18,
19.5]]])"]},{"cell_type":"code","execution_count":null,"metadata":{"id":"XlyXBSLFdOnY","outputId":"1d1e1bfd-f898-48dc-b370-
9cd1b012d0e6","colab":{"base_uri":"https://localhost:8080/"},"executionInfo":
{"status":"ok","timestamp":1710812605715,"user_tz":-345,"elapsed":476,"user":{"displayName":"Abhishek
Paudel","userId":"15094254969844955559"}}},"outputs":[{"output_type":"execute_result","data":{"text/plain":["(2, 2, 3)"]},"metadata":
{},"execution_count":21}],"source":["arr3.shape"]},{"cell_type":"markdown","metadata":{"id":"fvoyE6RpdOnY"},"source":["All the elements in a
numpy array have the same data type. You can check the data type of an array using the `.dtype` property."]},
{"cell_type":"code","execution_count":null,"metadata":{"id":"4X_CbrMKdOnY","outputId":"193377bb-9e56-4b48-98a1-e51c32b495d3"},"outputs":
[{"data":{"text/plain":["dtype('float64')"]},"execution_count":34,"metadata":{},"output_type":"execute_result"}],"source":["weights.dtype"]},
{"cell_type":"code","execution_count":null,"metadata":{"id":"zfmTemBCdOnY","outputId":"5fe0f834-fae6-4fcf-ae79-68b948a8c07b"},"outputs":
[{"data":{"text/plain":["dtype('int32')"]},"execution_count":35,"metadata":{},"output_type":"execute_result"}],"source":["climate_data.dtype"]},
{"cell_type":"markdown","metadata":{"id":"Q5xSdYSgdOnZ"},"source":["If an array contains even a single floating point number, all the other
elements are also converted to floats."]},{"cell_type":"code","execution_count":null,"metadata":{"id":"LSdebIQrdOnZ","outputId":"5d5fd2f7-45ef-
4ab9-a747-d19b12fb9dd5"},"outputs":[{"data":{"text/plain":["dtype('float64')"]},"execution_count":54,"metadata":
{},"output_type":"execute_result"}],"source":["arr3.dtype"]},{"cell_type":"markdown","metadata":{"id":"KFbNGr6GdOnZ"},"source":["We can now
compute the predicted yields of apples in all the regions, using a single matrix multiplication between `climate_data` (a 5x3 matrix) and `weights`
(a vector of length 3). Here's what it looks like visually:\n","\n"," \n","\n","You can learn about matrices and matrix multiplication by watching the
first 3-4 videos of this playlist: https://www.youtube.com/watch?v=xyAuNHPsq-g&list=PLFD0EB975BA0CC1E0&index=1 .\n","\n","We can use the
`np.matmul` function or the `@` operator to perform matrix multiplication."]},{"cell_type":"code","execution_count":null,"metadata":
{"id":"cKs6hsR9dOnZ"},"outputs":[],"source":["result_mat = np.matmul(climate_data, weights)"]},
{"cell_type":"code","execution_count":null,"metadata":{"id":"FQkdxNCudOnZ","outputId":"cce3c4fe-008a-474b-8ed5-6c1b9e8c72a9"},"outputs":
[{"data":{"text/plain":["(5,)"]},"execution_count":38,"metadata":{},"output_type":"execute_result"}],"source":["result_mat.shape"]},
{"cell_type":"code","execution_count":null,"metadata":{"id":"4hIZ5abedOnZ","outputId":"5efe035a-1e3f-479a-8c4e-26c95f3a0a38"},"outputs":
[{"data":{"text/plain":["array([56.8, 76.9, 81.9, 57.7, 74.9])"]},"execution_count":42,"metadata":{},"output_type":"execute_result"}],"source":["#magic
FUnction Numpy\n","#Otherwise @ operator basically used in Decorators\n","climate_data @ weights"]},{"cell_type":"markdown","metadata":
{"id":"2EEVhbiedOna"},"source":["## Working with CSV data files\n","\n","Numpy also provides helper functions reading from & writing to files.
Let's download a file `climate.txt`, which contains 10,000 climate measurements (temperature, rainfall & humidity) in the following
format:\n","\n","\n","```\n","temperature,rainfall,humidity\n","25.00,76.00,99.00\n","39.00,65.00,70.00\n","59.00,45.00,77.00\n","84.00,63.00,38.00\n",
format of storing data is known as *comma-separated values* or CSV.\n","\n","> **CSVs**: A comma-separated values (CSV) file is a delimited
text file that uses a comma to separate values. Each line of the file is a data record. Each record consists of one or more fields, separated by
commas. A CSV file typically stores tabular data (numbers and text) in plain text, in which case each line will have the same number of fields.
(Wikipedia)\n","\n","\n","To read this file into a numpy array, we can use the `genfromtxt` function."]},
{"cell_type":"code","execution_count":null,"metadata":{"id":"CSD0UlgCdOna","outputId":"73b76969-bb6f-4565-9919-8f8d29287aaf","colab":
{"base_uri":"https://localhost:8080/"},"executionInfo":{"status":"ok","timestamp":1710812833888,"user_tz":-345,"elapsed":5,"user":
{"displayName":"Abhishek Paudel","userId":"15094254969844955559"}}},"outputs":[{"output_type":"execute_result","data":{"text/plain":["
('climate.txt', )"]},"metadata":{},"execution_count":22}],"source":["import urllib.request\n","\n","urllib.request.urlretrieve(\n","
'https://gist.github.com/BirajCoder/a4ffcb76fd6fb221d76ac2ee2b8584e9/raw/4054f90adfd361b7aa4255e99c2e874664094cea/climate.csv',\n","
'climate.txt')"]},{"cell_type":"code","execution_count":null,"metadata":{"id":"AZJhHdnMdOna"},"outputs":[],"source":["climate_data =
np.genfromtxt('climate.txt', delimiter=',', skip_header=1)"]},{"cell_type":"code","execution_count":null,"metadata":
{"id":"C3J3mE40dOna","outputId":"843b7c80-84d0-4bc9-f86e-b1f90d52a92e","colab":{"base_uri":"https://localhost:8080/"},"executionInfo":
{"status":"ok","timestamp":1710812891183,"user_tz":-345,"elapsed":4,"user":{"displayName":"Abhishek
Paudel","userId":"15094254969844955559"}}},"outputs":[{"output_type":"execute_result","data":{"text/plain":["array([[25., 76., 99.],\n"," [39., 65.,
70.],\n"," [59., 45., 77.],\n"," ...,\n"," [99., 62., 58.],\n"," [70., 71., 91.],\n"," [92., 39., 76.]])"]},"metadata":{},"execution_count":25}],"source":
["climate_data"]},{"cell_type":"code","execution_count":null,"metadata":{"id":"BTSBtAcndOnb","outputId":"1ce5893e-58aa-4f1e-b9cd13eb5f9e06e7","colab":{"base_uri":"https://localhost:8080/"},"executionInfo":
{"status":"ok","timestamp":1710812897510,"user_tz":-345,"elapsed":494,"user":{"displayName":"Abhishek
Paudel","userId":"15094254969844955559"}}},"outputs":[{"output_type":"execute_result","data":{"text/plain":["(10000, 3)"]},"metadata":
{},"execution_count":26}],"source":["climate_data.shape"]},{"cell_type":"markdown","metadata":{"id":"G_G4DbqFdOnb"},"source":["We can now
perform a matrix multiplication using the `@` operator to predict the yield of apples for the entire dataset using a given set of weights."]},
{"cell_type":"code","execution_count":null,"metadata":{"id":"YrfUfhKvdOnb"},"outputs":[],"source":["weights = np.array([0.3, 0.2, 0.5])"]},
{"cell_type":"code","execution_count":null,"metadata":{"id":"kaj5BlgodOnb"},"outputs":[],"source":["yields = climate_data @ weights"]},
{"cell_type":"code","execution_count":null,"metadata":{"id":"ksttx9M1dOnc","outputId":"4c922d9c-24a2-4845-dcdc-a8472667fd87","colab":
{"base_uri":"https://localhost:8080/"},"executionInfo":{"status":"ok","timestamp":1710812919823,"user_tz":-345,"elapsed":455,"user":
{"displayName":"Abhishek Paudel","userId":"15094254969844955559"}}},"outputs":[{"output_type":"execute_result","data":{"text/plain":
["array([72.2, 59.7, 65.2, ..., 71.1, 80.7, 73.4])"]},"metadata":{},"execution_count":29}],"source":["yields"]},
{"cell_type":"code","execution_count":null,"metadata":{"id":"louzCFeXdOnc","outputId":"4d6d9edf-89f9-4a89-e9c2-ebc00dbe5abc","colab":
{"base_uri":"https://localhost:8080/"},"executionInfo":{"status":"ok","timestamp":1710812922525,"user_tz":-345,"elapsed":488,"user":
{"displayName":"Abhishek Paudel","userId":"15094254969844955559"}}},"outputs":[{"output_type":"execute_result","data":{"text/plain":["
(10000,)"]},"metadata":{},"execution_count":30}],"source":
["#https://numpy.org/doc/stable/reference/generated/numpy.ndarray.shape.html\n","yields.shape"]},{"cell_type":"markdown","metadata":
{"id":"YKT0oXCwdOnc"},"source":["Let's add the `yields` to `climate_data` as a fourth column using the [`np.concatenate`]
(https://numpy.org/doc/stable/reference/generated/numpy.concatenate.html) function."]},{"cell_type":"code","execution_count":null,"metadata":
{"id":"6pc4P3YadOnc"},"outputs":[],"source":["climate_results = np.concatenate((climate_data, yields.reshape(10000, 1)), axis=1)"]},
{"cell_type":"code","execution_count":null,"metadata":{"id":"a0Ui9W04dOnc","outputId":"2fb41648-96a1-41ba-8dc6-400338a0c93b"},"outputs":
[{"data":{"text/plain":["array([[25. , 76. , 99. , 72.2],\n"," [39. , 65. , 70. , 59.7],\n"," [59. , 45. , 77. , 65.2],\n"," ...,\n"," [99. , 62. , 58. , 71.1],\n"," [70. ,
71. , 91. , 80.7],\n"," [92. , 39. , 76. , 73.4]])"]},"execution_count":49,"metadata":{},"output_type":"execute_result"}],"source":["climate_results"]},
{"cell_type":"markdown","metadata":{"id":"vy9AHCc8dOnd"},"source":["There are a couple of subtleties here:\n","\n","* Since we wish to add new
columns, we pass the argument `axis=1` to `np.concatenate`. The `axis` argument specifies the dimension for concatenation.\n","\n","* The arrays
should have the same number of dimensions, and the same length along each except the dimension used for concatenation. We use the
[`np.reshape`](https://numpy.org/doc/stable/reference/generated/numpy.reshape.html) function to change the shape of `yields` from `(10000,)` to
`(10000,1)`.\n","\n","Here's a visual explanation of `np.concatenate` along `axis=1` (can you guess what `axis=0` results in?):\n","\n","
\n","\n","The best way to understand what a Numpy function does is to experiment with it and read the documentation to learn about its
arguments & return values. Use the cells below to experiment with `np.concatenate` and `np.reshape`."]},
{"cell_type":"code","execution_count":null,"metadata":{"id":"lkZGCdmUdOnd"},"outputs":[],"source":[]},
{"cell_type":"code","execution_count":null,"metadata":{"id":"9OrjCE9idOnd"},"outputs":[],"source":[]},
{"cell_type":"code","execution_count":null,"metadata":{"id":"jkH_TtdOdOnd"},"outputs":[],"source":[]},{"cell_type":"markdown","metadata":{"id":"wAXg7DWdOnd"},"source":["Let's write the final results from our computation above back to a file using the `np.savetxt` function."]},
{"cell_type":"code","execution_count":null,"metadata":{"id":"Qcpq3RMydOnd","outputId":"44118e09-1d7d-49c9-d319-46ab166c0827"},"outputs":
[{"data":{"text/plain":["array([[25. , 76. , 99. , 72.2],\n"," [39. , 65. , 70. , 59.7],\n"," [59. , 45. , 77. , 65.2],\n"," ...,\n"," [99. , 62. , 58. , 71.1],\n"," [70. ,
71. , 91. , 80.7],\n"," [92. , 39. , 76. , 73.4]])"]},"execution_count":53,"metadata":{},"output_type":"execute_result"}],"source":["climate_results"]},
{"cell_type":"code","execution_count":null,"metadata":{"id":"4JQhdXapdOne"},"outputs":[],"source":["np.savetxt('climate_results.txt',\n","
climate_results,\n"," fmt='%.2f',\n"," delimiter=',',\n"," header='temperature,rainfall,humidity,yeild_apples',\n"," comments='')"]},
{"cell_type":"markdown","metadata":{"id":"7hX4cMTkdOne"},"source":["The results are written back in the CSV format to the file
`climate_results.txt`.\n","\n","```\n","temperature,rainfall,humidity,yeild_apples\n","25.00,76.00,99.00,72.20\n","39.00,65.00,70.00,59.70\n","59.00,45
{"cell_type":"markdown","metadata":{"id":"is-UWJCrdOne"},"source":["Numpy provides hundreds of functions for performing operations on arrays.
Here are some commonly used functions:\n","\n","\n","* Mathematics: `np.sum`, `np.exp`, `np.round`, arithemtic operators\n","* Array
manipulation: `np.reshape`, `np.stack`, `np.concatenate`, `np.split`\n","* Linear Algebra: `np.matmul`, `np.dot`, `np.transpose`, `np.eigvals`\n","*
Statistics: `np.mean`, `np.median`, `np.std`, `np.max`\n","\n","> **How to find the function you need?** The easiest way to find the right function
for a specific operation or use-case is to do a web search. For instance, searching for \"How to join numpy arrays\" leads to [this tutorial on array
concatenation](https://cmdlinetips.com/2018/04/how-to-concatenate-arrays-in-numpy/).\n","\n","You can find a full list of array functions here:
https://numpy.org/doc/stable/reference/routines.html"]},{"cell_type":"markdown","metadata":{"id":"zal_3gBfdOne"},"source":["### Save and upload
your notebook\n","\n","Whether you're running this Jupyter notebook online or on your computer, it's essential to save your work from time to time.
You can continue working on a saved notebook later or share it with friends and colleagues to let them execute your code. [Jovian]
(https://www.jovian.ai) offers an easy way of saving and sharing your Jupyter notebooks online."]},{"cell_type":"markdown","metadata":
{"id":"gUkromXvdOne"},"source":["## Arithmetic operations, broadcasting and comparison\n","\n","Numpy arrays support arithmetic operators like
`+`, `-`, `*`, etc. You can perform an arithmetic operation with a single number (also called scalar) or with another array of the same shape.
Operators make it easy to write mathematical expressions with multi-dimensional arrays."]},{"cell_type":"code","execution_count":null,"metadata":
{"id":"P2oN1yItdOne"},"outputs":[],"source":["arr2 = np.array([[1, 2, 3, 4],\n"," [5, 6, 7, 8],\n"," [9, 1, 2, 3]])"]},
{"cell_type":"code","execution_count":null,"metadata":{"id":"P7cqsH3tdOnf"},"outputs":[],"source":["arr3 = np.array([[11, 12, 13, 14],\n"," [15, 16,
17, 18],\n"," [19, 11, 12, 13]])"]},{"cell_type":"code","execution_count":null,"metadata":{"id":"4BVbkG-qdOnf","outputId":"a5945f43-5bbf-41b9-f97d234ac8c8613b"},"outputs":[{"data":{"text/plain":["array([[ 4, 5, 6, 7],\n"," [ 8, 9, 10, 11],\n"," [12, 4, 5, 6]])"]},"execution_count":60,"metadata":
{},"output_type":"execute_result"}],"source":["# Adding a scalar\n","arr2 + 3"]},{"cell_type":"code","execution_count":null,"metadata":{"id":"zMjy8EidOnf","outputId":"904e07f1-f503-4f6d-cc1e-accc6abed487"},"outputs":[{"data":{"text/plain":["array([[10, 10, 10, 10],\n"," [10, 10, 10, 10],\n","
[10, 10, 10, 10]])"]},"execution_count":61,"metadata":{},"output_type":"execute_result"}],"source":["# Element-wise subtraction\n","arr3 - arr2"]},
{"cell_type":"code","execution_count":null,"metadata":{"id":"R9J6n640dOnf","outputId":"1da3eb40-4dab-43f9-a3ac-179ee2965f84"},"outputs":
[{"data":{"text/plain":["array([[0.5, 1. , 1.5, 2. ],\n"," [2.5, 3. , 3.5, 4. ],\n"," [4.5, 0.5, 1. , 1.5]])"]},"execution_count":62,"metadata":
{},"output_type":"execute_result"}],"source":["# Division by scalar\n","arr2 / 2"]},{"cell_type":"code","execution_count":null,"metadata":
{"id":"cvo6ncjidOnf","outputId":"3e52b832-0521-4045-c108-d01e343395bd"},"outputs":[{"data":{"text/plain":["array([[ 11, 24, 39, 56],\n"," [ 75, 96,
119, 144],\n"," [171, 11, 24, 39]])"]},"execution_count":63,"metadata":{},"output_type":"execute_result"}],"source":["# Element-wise
multiplication\n","arr2 * arr3"]},{"cell_type":"code","execution_count":null,"metadata":{"id":"TcCwLzCAdOnf","outputId":"6b6d0e01-0930-4a88-
e072-a5fed453b10e"},"outputs":[{"data":{"text/plain":["array([[1, 2, 3, 0],\n"," [1, 2, 3, 0],\n"," [1, 1, 2, 3]])"]},"execution_count":64,"metadata":
{},"output_type":"execute_result"}],"source":["# Modulus with scalar\n","arr2 % 4"]},{"cell_type":"markdown","metadata":
{"id":"MNXm0pomdOng"},"source":["### Array Broadcasting\n","\n","Numpy arrays also support *broadcasting*, allowing arithmetic operations
between two arrays with different numbers of dimensions but compatible shapes. Let's look at an example to see how it works."]},
{"cell_type":"code","execution_count":null,"metadata":{"id":"RLYTtGc2dOng"},"outputs":[],"source":["arr2 = np.array([[1, 2, 3, 4],\n"," [5, 6, 7,
8],\n"," [9, 1, 2, 3]])"]},{"cell_type":"code","execution_count":null,"metadata":{"id":"c6JPMV_0dOng","outputId":"8747fbf8-a683-421a-8bb1-
55ef9f34f718"},"outputs":[{"data":{"text/plain":["(3, 4)"]},"execution_count":66,"metadata":{},"output_type":"execute_result"}],"source":
["arr2.shape"]},{"cell_type":"code","execution_count":null,"metadata":{"id":"5Becl-LddOng"},"outputs":[],"source":["arr4 = np.array([4, 5, 6, 7])"]},
{"cell_type":"code","execution_count":null,"metadata":{"id":"GNVyUzdudOng","outputId":"aa42ef7a-ddd7-4d4d-a1b7-cb1b9a6c423c"},"outputs":
[{"data":{"text/plain":["(4,)"]},"execution_count":68,"metadata":{},"output_type":"execute_result"}],"source":["arr4.shape"]},
{"cell_type":"code","execution_count":null,"metadata":{"id":"8aMIZxERdOng","outputId":"e623bd8d-9258-4f1a-8d62-a5c410371278"},"outputs":
[{"data":{"text/plain":["array([[ 5, 7, 9, 11],\n"," [ 9, 11, 13, 15],\n"," [13, 6, 8, 10]])"]},"execution_count":69,"metadata":
{},"output_type":"execute_result"}],"source":["arr2 + arr4"]},{"cell_type":"markdown","metadata":{"id":"HMVq_1-jdOnh"},"source":["When the
expression `arr2 + arr4` is evaluated, `arr4` (which has the shape `(4,)`) is replicated three times to match the shape `(3, 4)` of `arr2`. Numpy
performs the replication without actually creating three copies of the smaller dimension array, thus improving performance and using lower
memory.\n","\n"," \n","\n","Broadcasting only works if one of the arrays can be replicated to match the other array's shape."]},
{"cell_type":"code","execution_count":null,"metadata":{"id":"2YfIzwyKdOnh"},"outputs":[],"source":["arr5 = np.array([7, 8])"]},
{"cell_type":"code","execution_count":null,"metadata":{"id":"jE0qfCqSdOnh","outputId":"3e3bde24-0a60-4226-c123-4ccd42ba028e"},"outputs":
[{"data":{"text/plain":["(2,)"]},"execution_count":71,"metadata":{},"output_type":"execute_result"}],"source":["arr5.shape"]},
{"cell_type":"code","execution_count":null,"metadata":{"id":"RFiq09sDdOnh","outputId":"8361553f-396b-4714-dce9-608148577132"},"outputs":
[{"ename":"ValueError","evalue":"operands could not be broadcast together with shapes (3,4) (2,) ","output_type":"error","traceback":
["\u001b[0;31m---------------------------------------------------------------------------\u001b[0m","\u001b[0;31mValueError\u001b[0m Traceback (most recent
call last)","\u001b[0;32m\u001b[0m in \u001b[0;36m\u001b[0;34m\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0marr2\u001b[0m
\u001b[0;34m+\u001b[0m
\u001b[0marr5\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m","\u001b[0;31mValueError\u001b[0m:
operands could not be broadcast together with shapes (3,4) (2,) "]}],"source":["arr2 + arr5"]},{"cell_type":"markdown","metadata":
{"id":"xNvtRkw_dOni"},"source":["In the above example, even if `arr5` is replicated three times, it will not match the shape of `arr2`. Hence `arr2 +
arr5` cannot be evaluated successfully. Learn more about broadcasting here: https://numpy.org/doc/stable/user/basics.broadcasting.html ."]},
{"cell_type":"markdown","metadata":{"id":"gKk2J-j_dOni"},"source":["### Array Comparison\n","\n","Numpy arrays also support comparison
operations like `==`, `!=`, `>` etc. The result is an array of booleans."]},{"cell_type":"code","execution_count":null,"metadata":
{"id":"BZE_KJ1bdOni"},"outputs":[],"source":["arr1 = np.array([[1, 2, 3], [3, 4, 5]])\n","arr2 = np.array([[2, 2, 3], [1, 2, 5]])"]},
{"cell_type":"code","execution_count":null,"metadata":{"id":"pRn8-cECdOni","outputId":"a6470500-e924-4777-a56e-3923fa92eec4"},"outputs":
[{"data":{"text/plain":["array([[False, True, True],\n"," [False, False, True]])"]},"execution_count":74,"metadata":
{},"output_type":"execute_result"}],"source":["arr1 == arr2"]},{"cell_type":"code","execution_count":null,"metadata":
{"id":"OdIHNALtdOnk","outputId":"079412d0-cc19-4652-fd68-4c38186ca2e4"},"outputs":[{"data":{"text/plain":["array([[ True, False, False],\n"," [
True, True, False]])"]},"execution_count":75,"metadata":{},"output_type":"execute_result"}],"source":["arr1 != arr2"]},
{"cell_type":"code","execution_count":null,"metadata":{"id":"I7Y24xb7dOnl","outputId":"ca14e786-dd78-4aae-95c9-900f31d2d8ec"},"outputs":
[{"data":{"text/plain":["array([[False, True, True],\n"," [ True, True, True]])"]},"execution_count":76,"metadata":
{},"output_type":"execute_result"}],"source":["arr1 >= arr2"]},{"cell_type":"code","execution_count":null,"metadata":
{"id":"WgcUKRjrdOnl","outputId":"0686ac59-ae11-4694-a1bc-ae919d547c4b"},"outputs":[{"data":{"text/plain":["array([[ True, False, False],\n","
[False, False, False]])"]},"execution_count":77,"metadata":{},"output_type":"execute_result"}],"source":["arr1 < arr2"]},
{"cell_type":"markdown","metadata":{"id":"gbejWYgrdOnl"},"source":["Array comparison is frequently used to count the number of equal elements
in two arrays using the `sum` method. Remember that `True` evaluates to `1` and `False` evaluates to `0` when booleans are used in arithmetic
operations."]},{"cell_type":"code","execution_count":null,"metadata":{"id":"l2W6K5SWdOnl","outputId":"8ef04129-b1dd-411e-b38b219e8a41d421"},"outputs":[{"data":{"text/plain":["3"]},"execution_count":78,"metadata":{},"output_type":"execute_result"}],"source":["(arr1 ==
arr2).sum()"]},{"cell_type":"markdown","metadata":{"id":"6VkF4wUudOnm"},"source":["## Array indexing and slicing\n","\n","Numpy extends
Python's list indexing notation using `[]` to multiple dimensions in an intuitive fashion. You can provide a comma-separated list of indices or
ranges to select a specific element or a subarray (also called a slice) from a Numpy array."]},
{"cell_type":"code","execution_count":null,"metadata":{"id":"8OX2eJnZdOnm"},"outputs":[],"source":["arr3 = np.array([\n"," [[11, 12, 13, 14],\n","
[13, 14, 15, 19]],\n","\n"," [[15, 16, 17, 21],\n"," [63, 92, 36, 18]],\n","\n"," [[98, 32, 81, 23],\n"," [17, 18, 19.5, 43]]])"]},
{"cell_type":"code","execution_count":null,"metadata":{"id":"ee_1-CsZdOnm","outputId":"f6e5355d-790c-4a21-e201-0a201d909ae3"},"outputs":
[{"data":{"text/plain":["(3, 2, 4)"]},"execution_count":52,"metadata":{},"output_type":"execute_result"}],"source":["arr3.shape"]},
{"cell_type":"code","execution_count":null,"metadata":{"id":"OyH8c_0CdOnm","outputId":"30a75262-ff0f-4a2d-9bc7-814ec90d9197"},"outputs":
[{"data":{"text/plain":["36.0"]},"execution_count":53,"metadata":{},"output_type":"execute_result"}],"source":["# Single element\n","arr3[1, 1, 2]"]},
{"cell_type":"code","execution_count":null,"metadata":{"id":"NgY9iFUodOnm","outputId":"51492784-6795-478c-9958-bcffa97c6c2d"},"outputs":
[{"data":{"text/plain":["array([[[15., 16.]],\n","\n"," [[98., 32.]]])"]},"execution_count":82,"metadata":{},"output_type":"execute_result"}],"source":["#
Subarray using ranges\n","arr3[1:, 0:1, :2]"]},{"cell_type":"code","execution_count":null,"metadata":{"id":"BTLic3A5dOnm","outputId":"8e7b9515-
bfc8-42db-fecb-100d3d048ae1"},"outputs":[{"data":{"text/plain":["array([18., 43.])"]},"execution_count":83,"metadata":
{},"output_type":"execute_result"}],"source":["# Mixing indices and ranges\n","arr3[1:, 1, 3]"]},
{"cell_type":"code","execution_count":null,"metadata":{"id":"WWv8GswOdOnn","outputId":"53370a72-98ab-4b19-9e19-a442d4154f83"},"outputs":
[{"data":{"text/plain":["array([[63. , 92. , 36. ],\n"," [17. , 18. , 19.5]])"]},"execution_count":84,"metadata":{},"output_type":"execute_result"}],"source":
["# Mixing indices and ranges\n","arr3[1:, 1, :3]"]},{"cell_type":"code","execution_count":null,"metadata":
{"id":"xTyfMnAsdOnn","outputId":"d12dd03f-2ead-448f-b76e-1e0ccbfab42f"},"outputs":[{"data":{"text/plain":["array([[15., 16., 17., 21.],\n"," [63.,
92., 36., 18.]])"]},"execution_count":85,"metadata":{},"output_type":"execute_result"}],"source":["# Using fewer indices\n","arr3[1]"]},
{"cell_type":"code","execution_count":null,"metadata":{"id":"gmljhTKCdOnn","outputId":"24dd70bc-8575-4464-bacf-7aa4c3c062f7"},"outputs":
[{"data":{"text/plain":["array([[13., 14., 15., 19.],\n"," [63., 92., 36., 18.]])"]},"execution_count":86,"metadata":
{},"output_type":"execute_result"}],"source":["# Using fewer indices\n","arr3[:2, 1]"]},{"cell_type":"code","execution_count":null,"metadata":
{"id":"hdnJuxyCdOnn","outputId":"9c50282d-8e6c-433d-ec68-72273679c90a"},"outputs":[{"ename":"IndexError","evalue":"too many indices for
array: array is 3-dimensional, but 4 were indexed","output_type":"error","traceback":["\u001b[0;31m--------------------------------------------------------------
-------------\u001b[0m","\u001b[0;31mIndexError\u001b[0m Traceback (most recent call last)","\u001b[0;32m\u001b[0m in
\u001b[0;36m\u001b[0;34m\u001b[0m\n\u001b[1;32m 1\u001b[0m \u001b[0;31m# Using too many
indices\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 2\u001b[0;31m
\u001b[0marr3\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;36m3\u001b[0m\u001b[0;34m,\u001
too many indices for array: array is 3-dimensional, but 4 were indexed"]}],"source":["# Using too many indices\n","arr3[1,3,2,1]"]},
{"cell_type":"markdown","metadata":{"id":"rdOakr2GdOno"},"source":["The notation and its results can seem confusing at first, so take your time to
experiment and become comfortable with it. Use the cells below to try out some examples of array indexing and slicing, with different
combinations of indices and ranges. Here are some more examples demonstrated visually:\n","\n"," "]},
{"cell_type":"code","execution_count":null,"metadata":{"id":"PInlqTwfdOno"},"outputs":[],"source":[]},
{"cell_type":"code","execution_count":null,"metadata":{"id":"wDSI0JKWdOno"},"outputs":[],"source":[]},
{"cell_type":"code","execution_count":null,"metadata":{"id":"qkL6z8iOdOno"},"outputs":[],"source":[]},
{"cell_type":"code","execution_count":null,"metadata":{"id":"bj-1_HQxdOno"},"outputs":[],"source":[]},{"cell_type":"markdown","metadata":
{"id":"71HZetPqdOnp"},"source":["## Other ways of creating Numpy arrays\n","\n","Numpy also provides some handy functions to create arrays of
desired shapes with fixed or random values. Check out the [official documentation](https://numpy.org/doc/stable/reference/routines.arraycreation.html) or use the `help` function to learn more."]},{"cell_type":"code","execution_count":null,"metadata":
{"id":"KhymNcR5dOnp","outputId":"d6442ffb-7e0b-4d2f-fb72-01b7a822dc65"},"outputs":[{"data":{"text/plain":["array([[0., 0.],\n"," [0., 0.],\n"," [0.,
0.]])"]},"execution_count":88,"metadata":{},"output_type":"execute_result"}],"source":["# All zeros\n","np.zeros((3, 2))"]},
{"cell_type":"code","execution_count":null,"metadata":{"id":"3KuZ9GZLdOnp","outputId":"9ca045b6-03aa-480e-d4c6-3fae586ec8d6"},"outputs":
[{"data":{"text/plain":["array([[[1., 1., 1.],\n"," [1., 1., 1.]],\n","\n"," [[1., 1., 1.],\n"," [1., 1., 1.]]])"]},"execution_count":54,"metadata":
{},"output_type":"execute_result"}],"source":["# All ones\n","np.ones([2, 2, 3])"]},{"cell_type":"code","execution_count":null,"metadata":
{"id":"VDmBESL1dOnp","outputId":"2f5c5a3e-ccff-427c-b617-61b291632212"},"outputs":[{"data":{"text/plain":["array([[1., 0., 0.],\n"," [0., 1., 0.],\n","
[0., 0., 1.]])"]},"execution_count":90,"metadata":{},"output_type":"execute_result"}],"source":["# Identity matrix\n","np.eye(3)"]},
{"cell_type":"code","execution_count":null,"metadata":{"id":"vlUYdjKOdOnp","outputId":"d30f28f2-af46-4f96-8d5b-7459416c2c53"},"outputs":
[{"data":{"text/plain":["array([0.8208279 , 0.93801216, 0.44954753, 0.17816933, 0.32049174])"]},"execution_count":91,"metadata":
{},"output_type":"execute_result"}],"source":["# Random vector\n","np.random.rand(5)"]},{"cell_type":"code","execution_count":null,"metadata":
{"id":"uJoWTOMVdOnp","outputId":"ba45d375-a301-4108-a7f9-c35e87d5bf33"},"outputs":[{"data":{"text/plain":["array([[ 0.83775 , 1.13851471,
-0.79147694],\n"," [ 0.56320765, 1.00386056, -0.42502339]])"]},"execution_count":92,"metadata":{},"output_type":"execute_result"}],"source":["#
Random matrix\n","np.random.randn(2, 3) # rand vs. randn - what's the difference?\n","# rand ---> Uniform Distribution\n","#randn ---> Normal
Distribution"]},{"cell_type":"code","execution_count":null,"metadata":{"id":"XpBiQJ6_dOnq","outputId":"9469b9d6-f844-4ee1-e852-
01b806849fbe"},"outputs":[{"data":{"text/plain":["array([[42, 42, 42],\n"," [42, 42, 42]])"]},"execution_count":93,"metadata":
{},"output_type":"execute_result"}],"source":["# Fixed value\n","np.full([2, 3], 42)"]},{"cell_type":"code","execution_count":null,"metadata":
{"id":"QI5Dkou5dOnq","outputId":"f154b5c0-5b15-4821-9088-37ea25e79f71"},"outputs":[{"data":{"text/plain":["array([10, 13, 16, 19, 22, 25, 28, 31,
34, 37, 40, 43, 46, 49, 52, 55, 58,\n"," 61, 64, 67, 70, 73, 76, 79, 82, 85, 88])"]},"execution_count":94,"metadata":
{},"output_type":"execute_result"}],"source":["# Range with start, end and step\n","np.arange(10, 90, 3)"]},
{"cell_type":"code","execution_count":null,"metadata":{"id":"zfvJ-GzndOnq","outputId":"804c5b7b-ce3f-4915-9c90-6e08bb5529a7","colab":
{"base_uri":"https://localhost:8080/"},"executionInfo":{"status":"ok","timestamp":1710751584003,"user_tz":-345,"elapsed":1755,"user":
{"displayName":"Abhishek Paudel","userId":"15094254969844955559"}}},"outputs":[{"output_type":"execute_result","data":{"text/plain":["array([ 3.,
6., 9., 12., 15., 18., 21., 24., 27.])"]},"metadata":{},"execution_count":20}],"source":["# Equally spaced numbers in a range\n","np.linspace(3, 27,
9)"]},{"cell_type":"markdown","metadata":{"id":"O0mP8jnAdOnq"},"source":["## Exercises\n","\n","Try the following exercises to become familiar
with Numpy arrays and practice your skills:\n","\n","- Assignment on Numpy array functions: https://jovian.ai/aakashns/numpy-arrayoperations\n","- (Optional) 100 numpy exercises: https://jovian.ai/aakashns/100-numpy-exercises\n"]},{"cell_type":"markdown","metadata":
{"id":"WZMerkD-dOnq"},"source":["## Summary and Further Reading\n","\n","With this, we complete our discussion of numerical computing with
Numpy. We've covered the following topics in this tutorial:\n","\n","- Going from Python lists to Numpy arrays\n","- Operating on Numpy
arrays\n","- Benefits of using Numpy arrays over lists\n","- Multi-dimensional Numpy arrays\n","- Working with CSV data files\n","- Arithmetic
operations and broadcasting\n","- Array indexing and slicing\n","- Other ways of creating Numpy arrays\n","\n","\n","Check out the following
resources for learning more about Numpy:\n","\n","- Official tutorial: https://numpy.org/devdocs/user/quickstart.html\n","- Numpy tutorial on
W3Schools: https://www.w3schools.com/python/numpy_intro.asp\n","- Advanced Numpy (exploring the internals): http://scipylectures.org/advanced/advanced_numpy/index.html\n","\n","You are ready to move on to the next tutorial: [Analyzing Tabular Data using Pandas]
(https://jovian.ai/aakashns/python-pandas-data-analysis)."]},{"cell_type":"markdown","metadata":{"id":"xd9Zn8r7dOnq"},"source":["## Questions
for Revision\n","\n","Try answering the following questions to test your understanding of the topics covered in this notebook:\n","\n","1. What is a
vector?\n","2. How do you represent vectors using a Python list? Give an example.\n","3. What is a dot product of two vectors?\n","4. Write a
function to compute the dot product of two vectors.\n","5. What is Numpy?\n","6. How do you install Numpy?\n","7. How do you import the
`numpy` module?\n","8. What does it mean to import a module with an alias? Give an example.\n","9. What is the commonly used alias for
`numpy`?\n","10. What is a Numpy array?\n","11. How do you create a Numpy array? Give an example.\n","12. What is the type of Numpy
arrays?\n","13. How do you access the elements of a Numpy array?\n","14. How do you compute the dot product of two vectors using Numpy?
\n","15. What happens if you try to compute the dot product of two vectors which have different sizes?\n","16. How do you compute the elementwise product of two Numpy arrays?\n","17. How do you compute the sum of all the elements in a Numpy array?\n","18. What are the benefits of
using Numpy arrays over Python lists for operating on numerical data?\n","19. Why do Numpy array operations have better performance
compared to Python functions and loops?\n","20. Illustrate the performance difference between Numpy array operations and Python loops using
an example.\n","21. What are multi-dimensional Numpy arrays?\n","22. Illustrate the creation of Numpy arrays with 2, 3, and 4
dimensions.\n","23. How do you inspect the number of dimensions and the length along each dimension in a Numpy array?\n","24. Can the
elements of a Numpy array have different data types?\n","25. How do you check the data type of the elements of a Numpy array?\n","26. What is
the data type of a Numpy array?\n","27. What is the difference between a matrix and a 2D Numpy array?\n","28. How do you perform matrix
multiplication using Numpy?\n","29. What is the `@` operator used for in Numpy?\n","30. What is the CSV file format?\n","31. How do you read
data from a CSV file using Numpy?\n","32. How do you concatenate two Numpy arrays?\n","33. What is the purpose of the `axis` argument of
`np.concatenate`?\n","34. When are two Numpy arrays compatible for concatenation?\n","35. Give an example of two Numpy arrays that can be
concatenated.\n","36. Give an example of two Numpy arrays that cannot be concatenated.\n","37. What is the purpose of the `np.reshape`
function?\n","38. What does it mean to “reshape” a Numpy array?\n","39. How do you write a numpy array into a CSV file?\n","40. Give some
examples of Numpy functions for performing mathematical operations.\n","41. Give some examples of Numpy functions for performing array
manipulation.\n","42. Give some examples of Numpy functions for performing linear algebra.\n","43. Give some examples of Numpy functions for
performing statistical operations.\n","44. How do you find the right Numpy function for a specific operation or use case?\n","45. Where can you
see a list of all the Numpy array functions and operations?\n","46. What are the arithmetic operators supported by Numpy arrays? Illustrate with
examples.\n","47. What is array broadcasting? How is it useful? Illustrate with an example.\n","48. Give some examples of arrays that are
compatible for broadcasting?\n","49. Give some examples of arrays that are not compatible for broadcasting?\n","50. What are the comparison
operators supported by Numpy arrays? Illustrate with examples.\n","51. How do you access a specific subarray or slice from a Numpy array?
\n","52. Illustrate array indexing and slicing in multi-dimensional Numpy arrays with some examples.\n","53. How do you create a Numpy array
with a given shape containing all zeros?\n","54. How do you create a Numpy array with a given shape containing all ones?\n","55. How do you
create an identity matrix of a given shape?\n","56. How do you create a random vector of a given length?\n","57. How do you create a Numpy
array with a given shape with a fixed value for each element?\n","58. How do you create a Numpy array with a given shape containing randomly
initialized elements?\n","59. What is the difference between `np.random.rand` and `np.random.randn`? Illustrate with examples.\n","60. What is
the difference between `np.arange` and `np.linspace`? Illustrate with examples.\n"]},{"cell_type":"code","execution_count":null,"metadata":
{"id":"j9IYRO5_dOnr"},"outputs":[],"source":[]}],"metadata":{"kernelspec":{"display_name":"Python 3.11.1 64-
bit","language":"python","name":"python3"},"language_info":{"codemirror_mode":
{"name":"ipython","version":3},"file_extension":".py","mimetype":"text/xpython","name":"python","nbconvert_exporter":"python","pygments_lexer":"ipython3","version":"3.11.1"},"vscode":{"interpreter":
{"hash":"2d2bed6d6593ad42ee37082a402ff318e0755fb5a5b734779ca37dde28cceef0"}},"colab":{"provenance":
[]}},"nbformat":4,"nbformat_minor":0}