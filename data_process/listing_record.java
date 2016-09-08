package code;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;

public class listing_record {
	
	String line;
	
	String timestamp;
	Double borrowerRate;
	String credit;
	String listKey;
	String status;
	String node;
	
	public listing_record(String line) throws ParseException {
		
		this.line = line;
		String[] features = this.line.split(",");
		
		String time = features[64];	

		Date date = new SimpleDateFormat("dd/MM/yyyy").parse(time);		
		long unixTimestamp = date.getTime()/1000;
		
		this.timestamp = String.valueOf(unixTimestamp);
		this.borrowerRate = Double.parseDouble(features[8]);
		this.credit = features[14];	
		this.listKey = features[0];
		this.status = features[5];
		this.node = features[81];
		
	}
}
