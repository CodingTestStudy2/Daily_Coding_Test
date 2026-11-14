/*
1. 아이디어:
   - 테이블 구조를 구현, 각 메소드에 맞게 로직을 구현한다

   - 자료구조
   - Map<String, Integer> => 각 테이블의 컬럼 개수 저장
   - Map<String, Integer> tableIdxs => 각 테이블 auto-increasement 규칙을 위한 idx값 저장
   - Map<String, Map<Integer, List<String>>> tableData => 실제 데이터 저장, 이때 Map<Integer, List<String>>인 이유는 row값을 o(1)안에 체크 필요해서

2. 시간복잡도: SQL:  
             Insert: O(1)
             Remove: O(1)
             Select: O(1)
             Export: O(특정 테이블 크기 N)

3. 자료구조/알고리즘: 구현, MAP
*/

class SQL {
    private Map<String, Integer> tableColumns = new HashMap<>();
    private Map<String, Integer> tableIdxs = new HashMap<>();
    private Map<String, Map<Integer, List<String>>> tableData = new HashMap<>();

    public SQL(List<String> names, List<Integer> columns) {
        int len = names.size();
       
        for(int i=0; i<len; i++) {
            String s = names.get(i);
            int c = columns.get(i);

            tableColumns.put(s,c);
            tableIdxs.put(s,1);

            Map<Integer, List<String>> tmp = new HashMap<>();

            tableData.put(s, tmp);
        }
    }
    
    // auto-increment 방식으로 행 증가 (id++)
    // row가 존재하지 않거나, 유효한 데이터가 아니면 false
    public boolean ins(String name, List<String> row) {
        Integer num = tableColumns.get(name);

        if(num == null) return false;
        if(num != row.size()) return false;

        int idx = tableIdxs.get(name);
        tableData.get(name).put(idx, row);

        tableIdxs.put(name, idx+1);

        return true;

    }
    
    // 행 제거
    // 유효하지 않으면 제거 안함
    public void rmv(String name, int rowId) {
        if(tableData.get(name) == null) return;
        if(tableData.get(name).get(rowId) == null) return;
        
        tableData.get(name).remove(rowId);
    }
    
    // 선택된 위치 value 반환
    // name이나 row, column이 유효하지 않으면 <null> 반환
    public String sel(String name, int rowId, int columnId) {
        if(tableData.get(name) == null) return "<null>";
        if(tableData.get(name).get(rowId) == null) return "<null>";
        if(columnId > tableColumns.get(name) || columnId < 1) return "<null>";

        return tableData.get(name).get(rowId).get(columnId-1);
    }
    
    // csv 형식으로 모든 행열 return 
    public List<String> exp(String name) { 
        List<String> output = new ArrayList<>();
        
        if(tableData.get(name) == null) return output;

        for(int key : tableData.get(name).keySet()) {
            StringBuilder sb = new StringBuilder();
            sb.append(key).append(',');
            for(String s : tableData.get(name).get(key)) sb.append(s).append(',');
            
            sb.deleteCharAt(sb.length()-1);
            output.add(sb.toString());
        }
        return output;
    }
}

/**
 * Your SQL object will be instantiated and called as such:
 * SQL obj = new SQL(names, columns);
 * boolean param_1 = obj.ins(name,row);
 * obj.rmv(name,rowId);
 * String param_3 = obj.sel(name,rowId,columnId);
 * List<String> param_4 = obj.exp(name);
 */