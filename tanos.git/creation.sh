nameid="$RANDOM-$RANDOM-$RANDOM-$RANDOM"
mkdir $nameid
cd $nameid
mkdir folder
echo "bar" > folder/foo
echo "foo" > folder/bar
echo barfoo > ./foobar
