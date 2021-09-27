import { ComponentFixture, TestBed } from '@angular/core/testing';

import { KpiViewComponent } from './kpi-view.component';

describe('KpiViewComponent', () => {
  let component: KpiViewComponent;
  let fixture: ComponentFixture<KpiViewComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ KpiViewComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(KpiViewComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
