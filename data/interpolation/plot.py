import matplotlib.pyplot as plt
import sys
import csv
import os
import numpy as np

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

plt.figure(figsize=(9, 8), dpi=300)
plt.subplots_adjust(
  top=0.93, bottom=0.11, left=0.08, right=0.98,
  hspace=0.4
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

def common(ax):
  plt.xlim(0, 22050)
  plt.ylim(0, 1.05)
  plt.xlabel("Frequency [Hz]")
  plt.ylabel("Gain")
  plt.axvline(x=22050/2, label="$f_{N1} = 11025$ Hz", c='black', ls=':')
  plt.legend()
  ax.yaxis.set_major_locator(plt.MultipleLocator(0.25))
  

def read_waveform(path):
  f = open(path, 'r')
  x = []
  y = []
  for i, line in enumerate(f.readlines()):
    x.append(float(i))
    y.append(float(line))
  return np.array(x), np.array(y)
  
def common_wf(ax, xy, xscale = 1):
  width = 26 * xscale
  x, y = xy[0][0:width], xy[1][0:width]
  plt.xlim(-1, width)
  plt.ylim(-1.1, 1.1)
  plt.xlabel("Sample Time")
  plt.ylabel("Sample Value")
  plt.bar(x, y, width=0, joinstyle='round', capstyle='round', linewidth=2, edgecolor='tab:blue')
  plt.plot(x, y, '.')
  # ax.yaxis.set_major_locator(plt.MultipleLocator(0.25))

ax = plt.subplot(221)
plt.title("(a) Original signal")
x, y = read_waveform("./waveform-pre.txt")
x, y = x[0::2] / 2, y[0::2]
common_wf(ax, (x,y), 1)

ax = plt.subplot(222)
plt.title("(b) After upsampling with N = 2")
x, y = read_waveform("./waveform-post.txt")
common_wf(ax, (x,y),2)

ax = plt.subplot(223)
plt.title("(c) Original signal")
x, y = read_tsv("./pre.txt")
y = 10 ** (y / 20)
one = np.max(y)
y = y / one
plt.plot(x, y, '-')
common(ax)

ax = plt.subplot(224)
plt.title("(d) After upsampling  with N = 2")
x, y = read_tsv("./post.txt")
y = 10 ** (y / 20)
y = y / one
plt.plot(x, y, '-')
common(ax)

plt.savefig("../../Pictures/interpolation.png")
plt.show()


# import tikzplotlib

# tikzplotlib.clean_figure()
# print(tikzplotlib.get_tikz_code())

