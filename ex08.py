import numpy as np

data = np.genfromtxt("./wine_quality/winequality-red.csv", delimiter=';', skip_header=1, dtype=np.float32)

print("data size: -", data.nbytes, "bytes")
# print(data)



data3 = data[:,[1,5,11]]
QUALITY, SULPHATE, PH, ALCOHOL= 11, 9, 8, 10
# print(data3)

print(
    "Is there any wine with a percentage of alcohol greater than 20% ?",
    "Yes." if np.any(data[:,ALCOHOL] > 20.) else "No."
)

print(
    "What is the average % of alcohol on all wines in the data set ?",
    np.average(data[:,ALCOHOL]), "%",
    np.nanmean(data[:,ALCOHOL]), "%"
)

print(
    "Compute the minimum",
    np.min(data[:,PH]),
    ", the maximum",
    np.max(data[:,PH]),
    ", the 25th percentile",
    np.percentile(data[:,PH],25),
    ", the 50th percentile",
    np.percentile(data[:,PH],50),
    ", the 75th percentile",
    np.percentile(data[:,PH],75),
    ", the mean of the pH",
    np.mean(data[:,PH]),
)

sul = data[:,SULPHATE]
q20 = np.percentile(sul,20)

quality = data[:,QUALITY][sul<=q20]

print(
    "Compute the average quality of the wines having the 20% least sulphates",
    np.average(quality)
)

quality = data[:,QUALITY]
max_qua = np.where(quality == np.max(quality))
min_qua = np.where(quality == np.min(quality))

print(
    "Compute the mean of all variables for wines having the best quality.\n",
    np.mean(data[max_qua], axis=0),
    "Compute the mean of all variables for wines having the worst quality.",
    np.mean(data[min_qua], axis=0),
)