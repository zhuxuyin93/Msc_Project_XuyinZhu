package code;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.text.ParseException;
import java.util.ArrayList;
import java.util.HashMap;

/* 
 * according to information like timestamp, credit rating, borrower rate, 
 * connect each record in the  network with corresponding loan.
 */

public class identify_graph_listing {
	
	public static void main(String[] args) throws IOException, ParseException {
		
		// open graph
		String graphPath = "/Users/zxy/Desktop/project/data/graph.txt";
		HashMap<String, graph_record> graphMap = new HashMap<String, graph_record>();
		
		File graphFile = new File(graphPath);
		BufferedReader graphReader = new BufferedReader(new FileReader(graphFile));
		String graphLine = null;	
		
		while((graphLine = graphReader.readLine()) != null) {  
			
			graph_record gRecord = new graph_record(graphLine);
			String mapKey = gRecord.target+","+gRecord.timestamp;
			
			if(!graphMap.containsKey(mapKey))
				graphMap.put(mapKey, gRecord);	
		}
		graphReader.close();
		System.out.println("finish loading graph");
		
		// open listing
		String listingPath = "/Users/zxy/Desktop/project/data/listing.csv";
		ArrayList<listing_record> listingList = new ArrayList<listing_record>();
		
		File listingFile = new File(listingPath);
		BufferedReader listingReader = new BufferedReader(new FileReader(listingFile));
		String listingLine = null;	
		
		while((listingLine = listingReader.readLine()) != null) {  
			
			listing_record lRecord = new listing_record(listingLine);
			listingList.add(lRecord);			
		}
		listingReader.close();	
		
		// identify data
		for(String key: graphMap.keySet()) {
			
			graph_record gRecord = graphMap.get(key);
			int count = 0;
			listing_record lRecord = null;
			
			for(int i=0; i<listingList.size();i++) {
				
				listing_record l = listingList.get(i);
				
				if(gRecord.timestamp.equals(l.timestamp) && gRecord.credit.equals(l.credit) &&  gRecord.borrowerRate.equals(l.borrowerRate)) {
					count = count + 1;
					lRecord = listingList.get(i);
				}
			}
			
			if(count == 1) {
				gRecord.listKey = lRecord.listKey;
				System.out.println(gRecord.listKey);
				
			}						
			else {
				gRecord.listKey = "notSure";
				System.out.println(gRecord.listKey);
			}						
		}
		
		// write results
		File out = new File("/Users/zxy/Desktop/project/data/identifyData.txt");
		BufferedWriter bfWrite = new BufferedWriter(new FileWriter(out));			
		for(String key: graphMap.keySet()) {
			graph_record g = graphMap.get(key);
			bfWrite.write(g.listKey+" "+g.source+" "+g.target+" "+g.weight+" "+g.timestamp+" "+g.amount+g.borrowerRate+" "+g.credit);
			bfWrite.newLine();
		}
		bfWrite.flush();
		bfWrite.close();
	}
}
		
		






		
		