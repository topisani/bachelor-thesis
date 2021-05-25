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

def do_plot(data):
  plt.xlim(0, 22050)
  plt.ylim(-100, 10)
  plt.xlabel("Frequency [Hz]")
  plt.ylabel("Magnitude [dB]")
  plt.plot(data[0], data[1], '-')
  plt.axvline(x=22050/2, label="$11025$ Hz", c='black', ls=':')
  plt.fill_between(data[0], data[1], -200)

plt.subplot(221)
plt.title("(a) SR = 176.4kHz, No oversampling")
do_plot(read_tsv("./176kX1_1.8kHz.txt"))
plt.legend()

plt.subplot(222)
plt.title("(b) SR = 22050Hz, No oversampling")
do_plot(read_tsv("./22kX1_1.8kHz.txt"))
plt.legend()
              
plt.subplot(223)
plt.title("(c) SR = 22050Hz, N = 2")
do_plot(read_tsv("22kX2_1.8kHz.txt"))
freq_resp = read_tsv("freq_resp_half.txt")
whitenoise = read_tsv("whitenoise.txt")
freq_resp = (freq_resp[0], freq_resp[1] - whitenoise[1])
plt.plot(freq_resp[0], freq_resp[1], '-', label="$F_i=F_d$")
plt.legend()

plt.subplot(224)
plt.title("(d) SR = 22050Hz, N = 4")
do_plot(read_tsv("22kX4_1.8kHz.txt"))
freq_resp = read_tsv("freq_resp_quarter.txt")
whitenoise = read_tsv("whitenoise88k.txt")
freq_resp = (freq_resp[0], freq_resp[1] - whitenoise[1])
plt.plot(freq_resp[0], freq_resp[1], '-', label="$F_i=F_d$")
plt.legend()

plt.savefig("../../Pictures/resampled_tanh.png")
# plt.show()


# import tikzplotlib

# tikzplotlib.clean_figure()
# print(tikzplotlib.get_tikz_code())

