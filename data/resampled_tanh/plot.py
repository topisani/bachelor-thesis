import matplotlib.pyplot as plt
import sys
import csv
import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

plt.figure(figsize=(9, 8), dpi=300)
plt.subplots_adjust(
  top=0.93, bottom=0.11, left=0.08, right=0.98,
  hspace=0.4
)
# plt.style.use("seaborn-darkgrid")
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
  return (x, y)

a = read_tsv("22.05kX2.txt")
b = read_tsv("freq_resp.txt")
c = read_tsv("96k.txt")

def do_plot(data):
  plt.xlim(0, 22050)
  plt.ylim(-150, 0)
  plt.xlabel("Frequency [Hz]")
  plt.ylabel("Magnitude [dB]")
  plt.plot(data[0], data[1], '-')
  #plt.fill_between(data[0], data[1], -200)
              
plt.subplot(221)
plt.title("SR = 22050Hz")
do_plot(a)
plt.axvline(x=22050/2, label="$f_N = 11025$", c='black', ls=':')
plt.legend()


plt.subplot(222)
plt.title("Filter Frequency Response, SR = 44100")
plt.axvline(x=22050/2, label="$f_S/4 = 11025$", c='black', ls=':')
plt.legend()
do_plot(b)

plt.subplot(223)
plt.title("SR = 96000Hz")
do_plot(c)

plt.minorticks_off()
# plt.grid(which="both", color="#aaaaaa")
plt.savefig("../../Pictures/resampled_tanh.png")
plt.show()


# import tikzplotlib

# tikzplotlib.clean_figure()
# print(tikzplotlib.get_tikz_code())

