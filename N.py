program DeretAngkaTanpaOutputLangsung;
uses crt;

var
  i, sum, addend: Integer;
  output: String;

begin
  i := 1;
  sum := 1; // Karena kita mulai dari 1+1
  addend := 0;
  output := ''; // Inisialisasi string output

  while i <= 5 do
  begin
    // Logika perbandingan untuk menentukan nilai yang ditambahkan
    case i of
      1: addend := 1;
      2: addend := 4;
      3: addend := 2;
      4: addend := 7;
      5: addend := 3;
    end;

    sum := sum + addend;

    // Menambahkan hasil ke string output
    output := output + IntToStr(sum) + ' ';

    // Increment counter
    i := i + 1;
  end;

  // Kode di sini untuk menggunakan string output sesuai kebutuhan Anda
  // Misalnya, menyimpannya ke file atau database, atau mengirimnya ke komponen GUI lain

  // Contoh: Menampilkan output ke TMemo (jika menggunakan Lazarus atau Delphi)
  // Memo1.Text := output;

  readln;
end.
