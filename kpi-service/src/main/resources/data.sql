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

INSERT INTO kpi(code, name,frequency_in_days, description, structural_element, unit_id) VALUES ('L2.N1.PN5.01','Tình hình phổ cập lớp học đa phương tiện tại trường học',120,'Đánh giá đô thị trong việc xây dựng môi trường học tập thông minh','District', 1);
INSERT INTO kpi(code, name,frequency_in_days, description, structural_element, unit_id) VALUES ('L2.N1.PN5.02','Tình hình ứng dụng ICT trong kết nối gia đình và nhà trường',120,'Đánh giá đô thị trong việc xây dựng môi trường học tập thông minh','District', 1);

INSERT INTO kpi(code, name,frequency_in_days, description, structural_element, unit_id) VALUES ('L2.N1.PN6.01','Tình hình phổ biến thông tin việc làm',120,'Đánh giá việc ứng dụng ICT nhằm phổ biến nhanh chóng thông tin việc làm','District', 1);
INSERT INTO kpi(code, name,frequency_in_days, description, structural_element, unit_id) VALUES ('L2.N1.PN6.02','Việc giải quyết dịch vụ việc làm trực tuyến',120,'Đánh giá việc ứng dụng ICT nhằm giải quyết việc làm cho người dân đô thị','District', 1);

INSERT INTO kpi(code, name,frequency_in_days, description, structural_element, unit_id) VALUES ('L2.N1.PN7.01','Tình hình cung cấp các dịch vụ đô thị qua Internet',120,'Đánh giá việc ứng dụng ICT nhằm giải quyết việc làm cho người dân đô thị','District', 1);
INSERT INTO kpi(code, name,frequency_in_days, description, structural_element, unit_id) VALUES ('L2.N1.PN7.02','Mức độ sử dụng dịch vụ đô thị qua Internet',120,'Đánh giá tình hình phát triển các dịch vụ hữu ích cho cư dân đô thị qua Internet','District', 1);

INSERT INTO kpi(code, name,frequency_in_days, description, structural_element, unit_id) VALUES ('L2.N1.PN8.01','Tình hình lập hồ sơ thông tin điện tử của các hộ gia đình khó khăn',120,'Đánh giá tình hình ứng dụng ICT vào trợ giúp nhóm người khó khăn, tàn tật, nghèo khó','District', 1);

INSERT INTO kpi(code, name,frequency_in_days, description, structural_element, unit_id) VALUES ('L2.N1.PN9.01','Tình hình ứng dụng ICT trong quản lý và vận hành mạng lưới cấp nước',120,'Đánh giá tình hình ứng dụng ICT vào hệ thống cung cấp nước sạch đô thị','District', 1);
INSERT INTO kpi(code, name,frequency_in_days, description, structural_element, unit_id) VALUES ('L2.N1.PN9.02','Tình hình sử dụng đồng hồ đo nước thông minh',120,'Đánh giá tình hình ứng dụng ICT vào hệ thống cung cấp nước sạch đô thị','District', 1);

INSERT INTO kpi(code, name,frequency_in_days, description, structural_element, unit_id) VALUES ('L2.N1.PN10.01','Tình hình cung cấp thông tin trực tuyến về tiêu thụ điện cho khách hàng',120,'Đánh giá tình hình ứng dụng ICT vào hệ thống cung cấp năng lượng đô thị','District', 1);
INSERT INTO kpi(code, name,frequency_in_days, description, structural_element, unit_id) VALUES ('L2.N1.PN10.02','Tình hình sử dụng công tơ điện thông minh',120,'Đánh giá tình hình ứng dụng ICT vào hệ thống cung cấp năng lượng đô thị','District', 1);

INSERT INTO kpi(code, name,frequency_in_days, description, structural_element, unit_id) VALUES ('L2.N2.PN1.01','Tình hình ứng dụng ICT trong quản lý tài sản công',120,'Đánh giá tình hình ứng dụng ICT vào quản lý hiệu quả các hoạt động nội bộ của CQĐT','District', 1);
INSERT INTO kpi(code, name,frequency_in_days, description, structural_element, unit_id) VALUES ('L2.N2.PN1.02','Tình hình ứng dụng ICT theo dõi hiệu quả các dự án đô thị',120,'Đánh giá tình hình ứng dụng ICT vào quản lý hiệu quả các hoạt động nội bộ của CQĐT','District', 1);

INSERT INTO kpi(code, name,frequency_in_days, description, structural_element, unit_id) VALUES ('L2.N2.PN2.01','Tình hình lắp đặt camera giám sát an ninh trật tự công cộng',120,'Đánh giá tình hình ứng dụng ICT vào giám sát an ninh trật tự đô thị','District', 1);
INSERT INTO kpi(code, name,frequency_in_days, description, structural_element, unit_id) VALUES ('L2.N2.PN2.02','Tình hình ứng dụng ICT trong công tác phòng cháy chữa cháy',120,'Đánh giá tình hình ứng dụng ICT vào công tác phòng cháy chữa cháy đô thị','District', 1);

INSERT INTO kpi(code, name,frequency_in_days, description, structural_element, unit_id) VALUES ('L2.N3.PN1.01','Tình hình ứng dụng ICT trong giám sát ô nhiễm đất đai',120,'Đánh giá tình hình ứng dụng ICT trong lĩnh vực bảo vệ môi trường đô thị','District', 1);
INSERT INTO kpi(code, name,frequency_in_days, description, structural_element, unit_id) VALUES ('L2.N3.PN1.02','Tình hình ứng dụng ICT theo dõi ô nhiễm nguồn nước',120,'Đánh giá tình hình ứng dụng ICT trong lĩnh vực bảo vệ môi trường đô thị','District', 1);
INSERT INTO kpi(code, name,frequency_in_days, description, structural_element, unit_id) VALUES ('L2.N3.PN1.03','Tình hình ứng dụng ICT theo dõi ô nhiễm không khí',120,'Đánh giá tình hình ứng dụng ICT trong lĩnh vực bảo vệ môi trường đô thị','District', 1);
INSERT INTO kpi(code, name,frequency_in_days, description, structural_element, unit_id) VALUES ('L2.N3.PN1.04','Tình hình ứng dụng ICT theo dõi ô nhiễm tiếng ồn',120,'Đánh giá tình hình ứng dụng ICT trong lĩnh vực bảo vệ môi trường đô thị','District', 1);
INSERT INTO kpi(code, name,frequency_in_days, description, structural_element, unit_id) VALUES ('L2.N3.PN1.05','Tình hình ứng dụng ICT giám sát xử lý nước thải',120,'Đánh giá tình hình ứng dụng ICT trong lĩnh vực bảo vệ môi trường đô thị','District', 1);

INSERT INTO kpi(code, name,frequency_in_days, description, structural_element, unit_id) VALUES ('L2.N3.PN2.01','Tình hình theo dõi thường xuyên các nguồn tiêu thụ năng lượng trọng điểm',120,'Đánh giá tình hình phát triển thành phố xanh, đẩy mạnh giảm tiêu hao năng lượng','District', 1);
INSERT INTO kpi(code, name,frequency_in_days, description, structural_element, unit_id) VALUES ('L2.N3.PN2.02','Tình hình sử dụng thiết bị chiếu sáng thông minh',120,'Đánh giá tình hình phát triển thành phố xanh, đẩy mạnh giảm tiêu hao năng lượng','District', 1);

INSERT INTO kpi(code, name,frequency_in_days, description, structural_element, unit_id) VALUES ('L3.N1.PN1.01','Tình hình phổ cập Wifi tại các điểm công cộng',200,'Đánh giá sự phát triển của hệ thống băng thông rộng cố định và đi động của đô thị','District', 1);
INSERT INTO kpi(code, name,frequency_in_days, description, structural_element, unit_id) VALUES ('L3.N1.PN1.02','Tình hình cung cấp mạng cáp quang đến khách hàng',200,'Đánh giá sự phát triển của hệ thống kết nối băng thông rộng cố định và đi động của đô thị','District', 1);
INSERT INTO kpi(code, name,frequency_in_days, description, structural_element, unit_id) VALUES ('L3.N1.PN1.03','Tình hình phổ cập băng rộng di động',200,'Đánh giá sự phát triển của hệ thống băng thông rộng cố định và đi động của đô thị','District', 1);

INSERT INTO kpi(code, name,frequency_in_days, description, structural_element, unit_id) VALUES ('L3.N1.PN2.01','Mức độ công khai tài nguyên thông tin công cộng tới xã hội',200,'Đánh giá mức độ công khai thông tin công cộng của đô thị trước xã hội','District', 1);
INSERT INTO kpi(code, name,frequency_in_days, description, structural_element, unit_id) VALUES ('L3.N1.PN2.02','Tình hình chia sẻ tài nguyên thông tin giữa các ngành quản lý của đô thị',200,'Đánh giá mức độ chia sẻ nguồn tài nguyên thông tin và mức độ công khai thông tin trước xã hội','District', 1);
INSERT INTO kpi(code, name,frequency_in_days, description, structural_element, unit_id) VALUES ('L3.N1.PN2.03','Tình hình khai thác sử dụng tài nguyên số thông qua sự hợp tác giữa doanh nghiệp và CQĐT',200,'Đánh giá mức độ chia sẻ tài nguyên số và mức độ công khai thông tin trước xã hội','District', 1);

INSERT INTO kpi(code, name,frequency_in_days, description, structural_element, unit_id) VALUES ('L3.N2.PN1.01','Tình hình đảm bảo an toàn thông tin',200,'Đánh giá năng lực đảm bảo an toàn thông tin cho các hệ thống thông tin quan trọng','District', 1);

INSERT INTO kpi(code, name,frequency_in_days, description, structural_element, unit_id) VALUES ('L3.N3.PN1.01','Sự chuẩn bị điều kiện về chính sách và pháp lý cho việc xây dựng ĐTTM',200,'Đánh giá sự sẵn sàng của CQĐT cho xây dựng ĐTTM','District', 1);
INSERT INTO kpi(code, name,frequency_in_days, description, structural_element, unit_id) VALUES ('L3.N3.PN1.02','Sự sẵn sàng về nguồn nhân lực ICT cho xây dựng ĐTTM',200,'Đánh giá sự sẵn sàng của CQĐT cho xây dựng ĐTTM','District', 1);
INSERT INTO kpi(code, name,frequency_in_days, description, structural_element, unit_id) VALUES ('L3.N3.PN1.03','Sự sẵn sàng về nguồn lực tài chính cho xây dựng ĐTTM',200,'Đánh giá sự sẵn sàng của CQĐT cho xây dựng ĐTTM','District', 1);

INSERT INTO kpi(code, name,frequency_in_days, description, structural_element, unit_id) VALUES ('L3.N4.PN1.01','Mức độ tham gia của người dân trong hoạt động đổi mới sáng tạo đô thị',200,'Đánh giá vai trò của người dân trong việc tạo ra sáng kiến góp phần xây dựng ĐTTM','District', 1);
INSERT INTO kpi(code, name,frequency_in_days, description, structural_element, unit_id) VALUES ('L3.N4.PN1.02','Mức độ cung cấp dịch vụ trực tuyến của doanh nghiệp',200,'Đánh giá điều kiện liên quan khác trong việc sẵn sàng xây dựng ĐTTM','District', 1);
INSERT INTO kpi(code, name,frequency_in_days, description, structural_element, unit_id) VALUES ('L3.N4.PN1.03','Tình hình huy động nguồn lực xã hội hóa cho xây dựng ĐTTM',200,'Đánh giá điều kiện liên quan khác trong việc sẵn sàng xây dựng ĐTTM','District', 1);

INSERT INTO category_kpi(kpi_id, category_id) VALUES (1,1);
INSERT INTO category_kpi(kpi_id, category_id) VALUES (2,2);
INSERT INTO category_kpi(kpi_id, category_id) VALUES (3,3);
INSERT INTO category_kpi(kpi_id, category_id) VALUES (4,4);
INSERT INTO category_kpi(kpi_id, category_id) VALUES (5,5);
INSERT INTO category_kpi(kpi_id, category_id) VALUES (6,6);
INSERT INTO category_kpi(kpi_id, category_id) VALUES (7,6);
INSERT INTO category_kpi(kpi_id, category_id) VALUES (8,6);
INSERT INTO category_kpi(kpi_id, category_id) VALUES (9,7);
INSERT INTO category_kpi(kpi_id, category_id) VALUES (10,7);
INSERT INTO category_kpi(kpi_id, category_id) VALUES (11,7);
INSERT INTO category_kpi(kpi_id, category_id) VALUES (12,8);
INSERT INTO category_kpi(kpi_id, category_id) VALUES (13,8);
INSERT INTO category_kpi(kpi_id, category_id) VALUES (14,9);
INSERT INTO category_kpi(kpi_id, category_id) VALUES (15,10);
INSERT INTO category_kpi(kpi_id, category_id) VALUES (16,10);
INSERT INTO category_kpi(kpi_id, category_id) VALUES (17,11);
INSERT INTO category_kpi(kpi_id, category_id) VALUES (18,11);
INSERT INTO category_kpi(kpi_id, category_id) VALUES (19,12);
INSERT INTO category_kpi(kpi_id, category_id) VALUES (20,12);
INSERT INTO category_kpi(kpi_id, category_id) VALUES (21,13);
INSERT INTO category_kpi(kpi_id, category_id) VALUES (22,14);
INSERT INTO category_kpi(kpi_id, category_id) VALUES (23,14);
INSERT INTO category_kpi(kpi_id, category_id) VALUES (24,15);
INSERT INTO category_kpi(kpi_id, category_id) VALUES (25,15);
INSERT INTO category_kpi(kpi_id, category_id) VALUES (26,16);
INSERT INTO category_kpi(kpi_id, category_id) VALUES (27,16);
INSERT INTO category_kpi(kpi_id, category_id) VALUES (28,17);
INSERT INTO category_kpi(kpi_id, category_id) VALUES (29,17);
INSERT INTO category_kpi(kpi_id, category_id) VALUES (30,18);
INSERT INTO category_kpi(kpi_id, category_id) VALUES (31,18);
INSERT INTO category_kpi(kpi_id, category_id) VALUES (32,18);
INSERT INTO category_kpi(kpi_id, category_id) VALUES (33,18);
INSERT INTO category_kpi(kpi_id, category_id) VALUES (34,18);
INSERT INTO category_kpi(kpi_id, category_id) VALUES (35,19);
INSERT INTO category_kpi(kpi_id, category_id) VALUES (36,19);
INSERT INTO category_kpi(kpi_id, category_id) VALUES (37,20);
INSERT INTO category_kpi(kpi_id, category_id) VALUES (38,20);
INSERT INTO category_kpi(kpi_id, category_id) VALUES (39,20);
INSERT INTO category_kpi(kpi_id, category_id) VALUES (40,21);
INSERT INTO category_kpi(kpi_id, category_id) VALUES (41,21);
INSERT INTO category_kpi(kpi_id, category_id) VALUES (42,21);
INSERT INTO category_kpi(kpi_id, category_id) VALUES (43,22);
INSERT INTO category_kpi(kpi_id, category_id) VALUES (44,23);
INSERT INTO category_kpi(kpi_id, category_id) VALUES (45,23);
INSERT INTO category_kpi(kpi_id, category_id) VALUES (46,23);
INSERT INTO category_kpi(kpi_id, category_id) VALUES (47,24);
INSERT INTO category_kpi(kpi_id, category_id) VALUES (48,24);
INSERT INTO category_kpi(kpi_id, category_id) VALUES (49,24);
