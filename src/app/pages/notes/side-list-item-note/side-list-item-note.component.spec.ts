import { ComponentFixture, TestBed } from '@angular/core/testing';
import { SideListItemNoteComponent } from './side-list-item-note.component';

describe('SideListItemNoteComponent', () => {
  let component: SideListItemNoteComponent;
  let fixture: ComponentFixture<SideListItemNoteComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [SideListItemNoteComponent],
    }).compileComponents();

    fixture = TestBed.createComponent(SideListItemNoteComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
