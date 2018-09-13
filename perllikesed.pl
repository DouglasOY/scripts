use strict;
use warnings;
use Path::Tiny qw(path);

# sed  -i 's/from/to/g' filename.txt
my $filename = "filename.txt";
my $file = path($filename);
my $data = $file->slurp_utf8;
$data =~ s/from/to/g;
$file->spew_utf8( $data );


# sed  -i 's/from/to/g' filename.txt
my $filename = $ARGV[0];
 
my $data = read_file($filename);
$data =~ s/from/to/g;
write_file($filename, $data);
exit;
 
sub read_file {
    my ($filename) = @_;
 
    open my $in, '<:encoding(UTF-8)', $filename or die "Could not open '$filename' for reading $!";
    local $/ = undef;
    my $all = <$in>;
    close $in;
 
    return $all;
}
 
sub write_file {
    my ($filename, $content) = @_;
 
    open my $out, '>:encoding(UTF-8)', $filename or die "Could not open '$filename' for writing $!";;
    print $out $content;
    close $out;
 
    return;
}


# sed -n '/xx/p' filename
my $filename = "filename.txt";
open (FILE, "<$filename") or die "Can't open file: $!\n";
while(my $line = <FILE>) {
    print "$line" if $line =~ /xx/;
}
close(FILE);



# sed -i '/pattern1/a\good' filename.txt
my $filename = "filename.txt";
my $epoc = time();
my $filenametmp = $filename."_tmp".$epoc;

open (ORIG, "<$filename") or die "Can't open file: $!\n";
open (TMP, ">$filenametmp") or die "Can't open file: $!\n";

while(my $line = <ORIG>) {
    if($line =~ /to/) { 
        print TMP $line . "oo------\npp======\n"; 
    } else {
        print TMP $line;
    }
}

close(ORIG);
close(TMP);

unlink $filename;
rename($filenametmp, $filename);

# sed -i '/pattern1/{s/pattern2/to/;}' filename.txt

my $filename = "filename.txt";
my $epoc = time();
my $filenametmp = $filename."_tmp".$epoc;

open (ORIG, "<$filename") or die "Can't open file: $!\n";
open (TMP, ">$filenametmp") or die "Can't open file: $!\n";

while(my $line = <ORIG>) {
    if($line =~ /oo|pp/) { 
        $line =~ s/----/\[\[\[/;
        $line =~ s/====/\]\]\]/;
        print TMP $line; 
    } else {
        print TMP $line;
    }
}

close(ORIG);
close(TMP);

unlink $filename;
rename($filenametmp, $filename);


# grep -o "xx" file
perl -ne "if(@list = /xx/gi) {print qq/@list,\n/;}" file

print "hello\n";

