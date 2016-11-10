# Split exam file into sensible chunks.
for i in {1..50}
do
  start_page=$(expr 22 \* $(expr $i - 1) + 1)
  end_page=$(expr 22 \* $i)
  echo Collating pages $start_page--$end_page
  #pdftk A=cs101-midterm1.pdf cat A$start_page-$end_page output cs101-midterm1-$i.pdf
done

# Print each with proper settings (including stapling).
lpc status CS-2313-LaserJet-M9040
for j in {1..4}  # 15*50 = 750, so some margin for error in distribution
do
  for i in {1..50}
  do
    lpr -P CS-2313-LaserJet-M9040 -staple -simplex cs101-midterm1-$i.pdf 
    #lpr -P siebl-1228-printer -staple -simplex cs101-midterm1-$i.pdf
  done
done
