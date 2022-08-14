def test_seed():
    sql = ("SELECT * FROM patents.patentData")
    cursor.execute(sql)
    # Fetch all the records
    result = cursor.fetchall()
    assert len(result)==30

def test_existence():
    sql = ("SELECT * FROM patents.patentData")
    cursor.execute(sql)
    result = cursor.fetchall()
    assert "DENTRY" in result

