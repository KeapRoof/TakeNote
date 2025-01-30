import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SideListNoteComponent } from './side-list-note.component';

describe('SideListNoteComponent', () => {
  let component: SideListNoteComponent;
  let fixture: ComponentFixture<SideListNoteComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [SideListNoteComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(SideListNoteComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
