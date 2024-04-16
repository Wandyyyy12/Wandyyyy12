program TabelPerkalianMemo;
uses Forms, StdCtrls;

var
  Form: TForm;
  Memo: TMemo;
  i, j: integer;

begin
  Application.Initialize;
  Form := TForm.Create(nil);
  Memo := TMemo.Create(Form);
  Memo.Parent := Form;
  Memo.Align := alClient;
  Form.Show;

  for i := 6 to 7 do
  begin
    for j := 0 to 6 do
    begin
      Memo.Lines.Add(IntToStr(i) + ' x ' + IntToStr(j) + ' = ' + IntToStr(i * j));
    end;
    Memo.Lines.Add('-------------------');
  end;

  Application.Run;
end.
