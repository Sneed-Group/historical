echo "<CONTENTS-BEGIN>"
docx2txt $1.docx
echo "<CONTENTS-END>"
cat $1.txt
rm $1.txt
