import matplotlib.pyplot as plt
import sys
import csv
import os
import numpy as np

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

plt.figure(figsize=(4, 3), dpi=300)
plt.subplots_adjust(
  top=0.955,
  bottom=0.125,
  left=0.16,
  right=0.999,
  hspace=0.2,
  wspace=0.2
)
plt.style.use("seaborn-darkgrid")
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    # "font.serif": ["Palatino"],
})
def read_tsv(path):
  x = []
  y = []
  with open(path) as tsvfile:
    tsvreader = csv.reader(tsvfile, delimiter="\t")
    titles = tsvreader.__next__()
    for line in tsvreader:
      x.append(float(line[0]))
      y.append(float(line[1]))
  return (np.array(x), np.array(y))
  
noise = read_tsv("noise.txt")
a25 = read_tsv("a.25.txt")
a50 = read_tsv("a.5.txt")
a75 = read_tsv("a.75.txt")

window = 64

def moving_average(x, w):
  return np.convolve(x, np.ones(w), 'same') / w
    
def do_plot(data, label):
  x, y = (data[0], data[1] - np.mean(noise[1]))
  y = moving_average(y, window)
  plt.plot(x[:-window], y[:-window], '-', label=label)
  
plt.xlim(0, 21400)
plt.ylim(-20, 5)
plt.xlabel("Frequency [Hz]")
plt.ylabel("Magnitude [dB]")

do_plot(a25, "$a = 0.25$")
do_plot(a50, "$a = 0.5$")
do_plot(a75, "$a = 0.75$")
plt.legend()

plt.savefig("../../Pictures/echo_filter_resp.png")
plt.show()


# import tikzplotlib

# tikzplotlib.clean_figure()
# print(tikzplotlib.get_tikz_code())

