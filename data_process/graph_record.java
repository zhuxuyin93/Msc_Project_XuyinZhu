package code;

public class graph_record {
	
	String line;
	
	String source;
	String target;
	String weight;
	String timestamp;
	String amount;
	Double borrowerRate;
	String credit;
	String listKey;
	
	public graph_record(String line) {
		
		this.line = line;
		String[] features = this.line.split(",");
		this.listKey = features[0];
		this.source = features[1];
		this.target = features[2];
		this.weight = features[3];
		this.timestamp = features[4];
		this.amount = features[5];
		this.borrowerRate = Double.parseDouble(features[6]);
		this.credit = features[7];	
	}
}
