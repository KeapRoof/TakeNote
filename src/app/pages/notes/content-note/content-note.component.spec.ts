import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ContentNoteComponent } from './content-note.component';

describe('ContentNoteComponent', () => {
  let component: ContentNoteComponent;
  let fixture: ComponentFixture<ContentNoteComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ContentNoteComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ContentNoteComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
