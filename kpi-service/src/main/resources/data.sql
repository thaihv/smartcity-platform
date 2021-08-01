-- The first level classification (in term of Class-Lớp in QD-3098 ) 
INSERT INTO classtype(code, name) VALUES ('L1','Lấy người dân làm trung tâm');
INSERT INTO classtype(code, name) VALUES ('L2','Hoạt động hiệu quả của bộ máy Chính quyền Đô Thị');
INSERT INTO classtype(code, name) VALUES ('L3','Định hướng và thúc đẩy');
-- The second level classification (in term of Group-Nhóm in QD-3098 )
INSERT INTO classification(code, name, classtype_id) VALUES ('L1.N1', 'Chia sẻ thông tin và lắng nghe ý kiến cư dân đô thị',1);
INSERT INTO classification(code, name, classtype_id) VALUES ('L1.N2', 'Tạo điều kiện cho người dân đô thị tham gia xây dựng ĐTTM',1);
INSERT INTO classification(code, name, classtype_id) VALUES ('L1.N3', 'Cảm nhận của người dân đô thị',1);
INSERT INTO classification(code, name, classtype_id) VALUES ('L2.N1', 'Dịch vụ tiện ích ĐTTM',2);
INSERT INTO classification(code, name, classtype_id) VALUES ('L2.N2', 'Quản lý đô thị hiệu quả',2);
INSERT INTO classification(code, name, classtype_id) VALUES ('L2.N3', 'Bảo vệ môi trường',2);
INSERT INTO classification(code, name, classtype_id) VALUES ('L3.N1', 'Hạ tầng thông tin',3);
INSERT INTO classification(code, name, classtype_id) VALUES ('L3.N2', 'An toàn thông tin',3);
INSERT INTO classification(code, name, classtype_id) VALUES ('L3.N3', 'Sự chuẩn bị nguồn lực cho xây dựng',3);
INSERT INTO classification(code, name, classtype_id) VALUES ('L3.N4', 'Đổi mới sáng tạo và tính mở của đô thị',3);
-- The third level classification (in term of Group-Phân nhóm in QD-3098 )
INSERT INTO category(code, name, classification_id) VALUES ('L1.N1.PN1', 'Dân biết',1);
INSERT INTO category(code, name, classification_id) VALUES ('L1.N1.PN2', 'Dân bàn',1);
INSERT INTO category(code, name, classification_id) VALUES ('L1.N1.PN3', 'Dân kiểm tra, giám sát',1);
INSERT INTO category(code, name, classification_id) VALUES ('L1.N2.PN1', 'Người dân tham gia phản hồi thông tin cho CQĐT',2);
INSERT INTO category(code, name, classification_id) VALUES ('L1.N3.PN1', 'Cảm nhận của người dân về tiến bộ của đô thị ',3);
INSERT INTO category(code, name, classification_id) VALUES ('L2.N1.PN1', 'Dịch vụ công',4);
INSERT INTO category(code, name, classification_id) VALUES ('L2.N1.PN2', 'Dịch vụ giao thông',4);
INSERT INTO category(code, name, classification_id) VALUES ('L2.N1.PN3', 'Dịch vụ y tế',4);
INSERT INTO category(code, name, classification_id) VALUES ('L2.N1.PN4', 'Dịch vụ an toàn vệ sinh thực phẩm',4);
INSERT INTO category(code, name, classification_id) VALUES ('L2.N1.PN5', 'Dịch vụ giáo dục',4);
INSERT INTO category(code, name, classification_id) VALUES ('L2.N1.PN6', 'Dịch vụ việc làm',4);
INSERT INTO category(code, name, classification_id) VALUES ('L2.N1.PN7', 'Các dịch vụ đô thị',4);
INSERT INTO category(code, name, classification_id) VALUES ('L2.N1.PN8', 'Dịch vụ an sinh xã hội',4);
INSERT INTO category(code, name, classification_id) VALUES ('L2.N1.PN9', 'Dịch vụ cung cấp nước sạch',4);
INSERT INTO category(code, name, classification_id) VALUES ('L2.N1.PN10', 'Dịch vụ cung cấp điện',4);
INSERT INTO category(code, name, classification_id) VALUES ('L2.N2.PN1', 'Công tác quản lý đô thị',5);
INSERT INTO category(code, name, classification_id) VALUES ('L2.N2.PN2', 'An ninh trật tự và PCCC của đô thị',5);
INSERT INTO category(code, name, classification_id) VALUES ('L2.N3.PN1', 'Bảo vệ môi trường',6);
INSERT INTO category(code, name, classification_id) VALUES ('L2.N3.PN2', 'Tiết kiệm năng lượng',6);
INSERT INTO category(code, name, classification_id) VALUES ('L3.N1.PN1', 'Hạ tầng thông tin băng thông rộng',7);
INSERT INTO category(code, name, classification_id) VALUES ('L3.N1.PN2', 'Chia sẻ tài nguyên',7);
INSERT INTO category(code, name, classification_id) VALUES ('L3.N2.PN1', 'An toàn thông tin',8);
INSERT INTO category(code, name, classification_id) VALUES ('L3.N3.PN1', 'Chính sách nhân lực và tài chính cho xây dựng ĐTTM',9);
INSERT INTO category(code, name, classification_id) VALUES ('L3.N4.PN1', 'Thúc đẩy, định hướng các điều kiện hỗ trợ xây dựng ĐTTM',10);
-- The unit of KPI measurement
INSERT INTO unit(name, symbol) VALUES ('Phần trăm', '%'); 
INSERT INTO unit(name, symbol) VALUES ('Điểm giám sát/Km²', '');
INSERT INTO unit(name, symbol) VALUES ('Có/Chưa', '');
INSERT INTO unit(name, symbol) VALUES ('Degree Celsius', 'ºC');
INSERT INTO unit(name, symbol) VALUES ('Watt hour', 'Wh');
INSERT INTO unit(name, symbol) VALUES ('Watt', 'W');
-- The KPI and its category (in term of Indicators Category- Chỉ số và Phân nhóm)
INSERT INTO kpi(code, name,frequency_in_days, description, structural_element, unit_id) VALUES ('L1.N1.PN1.01','Tình hình công khai thông tin đô thị cho người dân',1,'Đánh giá mức độ công khai thông tin, sự cầu thị của CQĐT','District', 1);
INSERT INTO kpi(code, name,frequency_in_days, description, structural_element, unit_id) VALUES ('L1.N1.PN2.01','Việc công khai kết quả phản hồi của người dân về hoạt động của CQDT',1,'Đánh giá việc thực hiện công khai thông tin phản hồi của người dân về hoạt động của CQĐT','District', 1);
INSERT INTO kpi(code, name,frequency_in_days, description, structural_element, unit_id) VALUES ('L1.N1.PN3.01','Mức độ thường xuyên đánh giá sự hài lòng của người dân',1,'Đánh giá mức độ quan tâm đến sự hài lòng của người dân','District', 1);
INSERT INTO kpi(code, name,frequency_in_days, description, structural_element, unit_id) VALUES ('L1.N2.PN1.01','Sự sẵn sàng của hạ tầng giúp người dân tham gia phản hồi thông tin cho CQĐT',1,'Đánh giá mức độ sẵn sàng của hạ tầng ICT cho phép người dân tham gia đóng góp ý kiến cho công tác quản lý đô thị','District', 1);
INSERT INTO kpi(code, name,frequency_in_days, description, structural_element, unit_id) VALUES ('L1.N3.PN1.01','Đánh giá chung của người dân về sự tiến bộ của đô thị',365,'Đánh giá sự hài lòng của người dân về sự tiến bộ của đô thị nói chung, không xét vấn đề cụ thể','District', 1);

INSERT INTO kpi(code, name,frequency_in_days, description, structural_element, unit_id) VALUES ('L2.N1.PN1.01','Tình hình sử dụng một mã số điện tử trong các dịch vụ hành chính công',90,'Đánh giá việc thực hiện cải cách hành chính của đô thị','District', 1);
INSERT INTO kpi(code, name,frequency_in_days, description, structural_element, unit_id) VALUES ('L2.N1.PN1.02','Mức độ ứng dụng ICT trong cung cấp dịch vụ công trực tuyến',90,'Đánh giá việc thực hiện cải cách hành chính của đô thị','District', 1);
INSERT INTO kpi(code, name,frequency_in_days, description, structural_element, unit_id) VALUES ('L2.N1.PN1.03','Hỗ trợ thực hiện thủ tục hành chính ứng dụng ICT',90,'Đánh giá việc thực hiện cải cách hành chính của đô thị','District', 1);
INSERT INTO kpi(code, name,frequency_in_days, description, structural_element, unit_id) VALUES ('L2.N1.PN2.01','Tình hình cung cấp thông tin giao thông thời gian thực',90,'Đánh giá sự ứng dụng ICT phục vụ giao thông và chất lượng giao thông công cộng','District', 1);
INSERT INTO kpi(code, name,frequency_in_days, description, structural_element, unit_id) VALUES ('L2.N1.PN2.02','Tình hình ứng dụng ICT trong các bãi đỗ xe',90,'Đánh giá sự ứng dụng ICT và chất lượng dịch vụ đỗ xe của CQĐT','District', 1);
INSERT INTO kpi(code, name,frequency_in_days, description, structural_element, unit_id) VALUES ('L2.N1.PN2.03','Tình hình ứng dụng ICT hỗ trợ giám sát chất lượng dịch vụ giao thông công cộng',90,'Đánh giá sự ứng dụng ICT để giám sát chất lượng dịch vụ giao thông công cộng trên địa bàn đô thị','District', 1);

INSERT INTO kpi(code, name,frequency_in_days, description, structural_element, unit_id) VALUES ('L2.N1.PN3.01','Tình hình sử dụng bệnh án điện tử',120,'Đánh giá sự ứng dụng ICT vào việc chăm sóc sức khỏe và hiệu quả dịch vụ y tế','District', 1);
INSERT INTO kpi(code, name,frequency_in_days, description, structural_element, unit_id) VALUES ('L2.N1.PN3.02','Tình hình ứng dụng ICT trong đăng ký khám chữa bệnh',120,'Đánh giá sự ứng dụng ICT vào việc chăm sóc sức khỏe và hiệu quả dịch vụ y tế','District', 1);

INSERT INTO kpi(code, name,frequency_in_days, description, structural_element, unit_id) VALUES ('L2.N1.PN4.01','Tình hình công khai thông tin nguồn gốc hàng hóa sản phẩm',120,'Đánh giá sự ứng dụng ICT vào việc đảm bảo an toàn vệ sinh thực phẩm','District', 1);

INSERT INTO category_kpi(kpi_id, category_id) VALUES (1,1);
INSERT INTO category_kpi(kpi_id, category_id) VALUES (2,2);
INSERT INTO category_kpi(kpi_id, category_id) VALUES (3,3);
INSERT INTO category_kpi(kpi_id, category_id) VALUES (4,4);
INSERT INTO category_kpi(kpi_id, category_id) VALUES (5,5);
INSERT INTO category_kpi(kpi_id, category_id) VALUES (6,6);
INSERT INTO category_kpi(kpi_id, category_id) VALUES (7,7);
INSERT INTO category_kpi(kpi_id, category_id) VALUES (8,8);
INSERT INTO category_kpi(kpi_id, category_id) VALUES (9,9);
INSERT INTO category_kpi(kpi_id, category_id) VALUES (10,10);
INSERT INTO category_kpi(kpi_id, category_id) VALUES (11,11);
INSERT INTO category_kpi(kpi_id, category_id) VALUES (12,12);
INSERT INTO category_kpi(kpi_id, category_id) VALUES (13,13);
INSERT INTO category_kpi(kpi_id, category_id) VALUES (14,14);












