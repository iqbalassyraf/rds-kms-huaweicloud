# rds-kms-huaweicloud
This is testing how a KMS on RDS for MySQL wokrs. The application hosted on ECS.

Set up your network infrastructure
1. Create VPC
2. Create Subnet. Recommendation use N-Tier architecture.
   - a subnet for frontend app
   - a subnet for backend (logic) app
   - a subnet for DB
   An n-tier application architecture is advantageous for several reasons. Firstly, it promotes modularity and scalability by separating the application into multiple layers, such as presentation, business logic, and data access, each handling specific tasks independently. This division enables easier maintenance, updates, and debugging as changes made in one layer do not necessarily affect the others. Additionally, n-tier architectures facilitate distributed deployment, allowing different layers to run on separate servers or even in different locations, enhancing performance, fault tolerance, and scalability. Lastly, the separation of concerns inherent in n-tier architectures improves code reusability and promotes a more organized and manageable development process, ultimately leading to higher-quality software products.

Set up the resources
1. Purchase ECS, for each function (frontend and backend) and place it on the respective subnet you created earlier.
2. Purchase RDS for MySQL
   - Add KMS during creation. Huawei Cloud Key Management Service (KMS) provides centralized management for encrypting data and managing encryption keys securely. By leveraging KMS, organizations can ensure data security and compliance by encrypting sensitive information and managing encryption keys effectively. With features such as easy integration with other Huawei Cloud services and simplified key management processes, KMS enables organizations to protect their data at rest and in transit while maintaining control over encryption keys, thereby enhancing overall data security and regulatory compliance.
   - Now your data at rest will be encrypted using KMS.
  
Access to Database:
You can use Data Admin Service, it's a centralized database o&M platform with build in security features, online debug, and visualization.

Establish connection from Backend ECS to RDS for MySQL.
1. Security group
   - See the security group you apply for both ecs and RDS. Allow inbound and outbound traffic from each IP address of the ECS and RDS, the port should be 3306 (Default port).
2. Customize your application code to access RDS for MySQL (Code example, see on Master branch).
3. Install the necessary dependencies on your ECS such as my.sql.connector or other that suits your application needs.

For more information contact:
Iqbal Assyraf
Huawei Cloud Solution Architect
iqbal.assyraf@huawei.com
