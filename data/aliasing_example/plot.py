import matplotlib.pyplot as plt
import sys
import csv
import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

plt.figure(figsize=(9, 4), dpi=300)
plt.subplots_adjust(
  top=0.93, bottom=0.11, left=0.08, right=0.98
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

a = read_tsv("11.025k.txt")
b = read_tsv("48k.txt")

def do_plot(data):
  plt.xlim(0, 11025)
  plt.ylim(-150, 0)
  plt.xlabel("Frequency [Hz]")
  plt.ylabel("Magnitude [dB]")
  plt.plot(data[0], data[1], '-')
  plt.fill_between(data[0], data[1], -200)
  plt.annotate('Base Frequency', xy=(440, -18), xytext=(2000, -10),
               arrowprops=dict(arrowstyle="->", color="black", connectionstyle="arc3"),
              )
              
plt.subplot(121)
plt.title("SR = 11025Hz")
do_plot(a)
plt.axvline(x=11025/2, label="$f_N$", c='black', ls=':')
plt.legend()


plt.subplot(122)
plt.title("SR = 96000Hz")
do_plot(b)

plt.minorticks_off()
# plt.grid(which="both", color="#aaaaaa")
plt.savefig("../../Pictures/aliasing_example.png")
plt.show()


# import tikzplotlib

# tikzplotlib.clean_figure()
# print(tikzplotlib.get_tikz_code())

