package lecture;

import java.util.ArrayList;
import java.util.Collections;

public class array_list {

	public static void main(String[] args) {
		ArrayList myList = new ArrayList(5);
		myList.add(3);
		myList.add(5);
		myList.add(510);
		myList.add(58);
		myList.add(51);
		myList.add(1);
		myList.add(89);
		myList.add(7);
		
		ArrayList myList2 = new ArrayList(1);
		myList2.add(4);
		myList.addAll(myList2);
		
		Collections.sort(myList);
		
		
		ArrayList newList = new ArrayList(myList.subList(0, 7)); // 인덱스 시작 부터 n-1까지 
		myList.remove(0);
		myList.clear();
		
		
		System.out.println(myList);
		System.out.println(newList);
		
		ArrayList mList = new ArrayList();
		for (int i = 0; i < 10; i++) {
			mList.add(i);
		}
		mList.add(mList.size(), "JAVA COllection");
		mList.add(3, "TEST");
		
		ArrayList<ArrayList<String>> kList = new ArrayList(); // [ []  ]
		
		ArrayList<String> jList = new ArrayList(); // []
		jList.add("abc");
		jList.add("cdfd");
		ArrayList<String> lList = new ArrayList(); // []
		lList.add("cdfd");
		lList.add("cdfd");
		
		
		
		kList.add(jList);
		kList.add(lList);
		
		System.out.println(kList);
		
		ArrayList list = new ArrayList();
		list.add(0);
		list.add(1);
		list.add(null);
		System.out.println( ((int)list.get(0)) + ((int)list.get(1)) );
		
	}

}

