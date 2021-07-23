INSERT INTO classtype(code, name) VALUES ('L1','Lấy người dân làm trung tâm');
INSERT INTO classtype(code, name) VALUES ('L2','Hoạt động hiệu quả của bộ máy Chính quyền Đô Thị');
INSERT INTO classtype(code, name) VALUES ('L3','Định hướng và thúc đẩy');

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


--INSERT INTO kpi(name,category_id) VALUES ('Test 1');