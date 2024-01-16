echo processing...
doc2odt $1.doc
echo "<CONTENTS-BEGIN>"
odt2txt $1.odt
echo "<CONTENTS-END>"
rm $1.odt
