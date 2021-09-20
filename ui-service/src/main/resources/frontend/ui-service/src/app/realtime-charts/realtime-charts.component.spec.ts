import { ComponentFixture, TestBed } from '@angular/core/testing';

import { RealtimeChartsComponent } from './realtime-charts.component';

describe('RealtimeChartsComponent', () => {
  let component: RealtimeChartsComponent;
  let fixture: ComponentFixture<RealtimeChartsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ RealtimeChartsComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(RealtimeChartsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
