public class KinesisComponentIntegrationTest extends CamelTestSupport {

    @BindToRegistry("amazonKinesisClient")
    AmazonKinesis client = AmazonKinesisClientBuilder.standard().withRegion(Regions.EU_CENTRAL_1).build();
    AmazonKinesis client = AmazonKinesisClientBuilder.standard().withRegion(Regions.EU_WEST_1).withCredentials(new AWSStaticCredentialsProvider(new BasicAWSCredentials("AKIAIHMCLOA573Z7SKYQ", "DC1Ow3nyac3/2OHV7zLl57oC7hnLPOB1BTtrUQGI"))).build();
