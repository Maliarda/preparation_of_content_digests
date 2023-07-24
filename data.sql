--
-- PostgreSQL database dump
--

-- Dumped from database version 14.6
-- Dumped by pg_dump version 14.6

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.alembic_version (version_num) FROM stdin;
26a314367f93
\.


--
-- Data for Name: user; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."user" (user_id, name) FROM stdin;
aad52838-848f-4e4f-b275-753fe0043102	sneakyfox
725c9545-2abf-4911-bb24-72d68c062f2b	grumpycat
308723fe-036c-4e40-b376-4d07ece516dd	friendlycapibara
\.


--
-- Data for Name: digest; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.digest (id, user_id, created_at) FROM stdin;
\.


--
-- Data for Name: subscription; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.subscription (id, source_name, user_id) FROM stdin;
1	Fashion is my profession	725c9545-2abf-4911-bb24-72d68c062f2b
2	Animal Planet	aad52838-848f-4e4f-b275-753fe0043102
3	Animal Planet	308723fe-036c-4e40-b376-4d07ece516dd
\.


--
-- Data for Name: post; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.post (id, subscription_id, text, popularity, created_at) FROM stdin;
1	1	Революция в моде: Одежда из переработанных материалов становится главным трендом. Дизайнеры представили уникальные коллекции, вдохновленные экологичностью. Новые веяния популяризуют сознательное потребление и устойчивую моду.	70	2023-07-22 05:26:08.216731
2	1	Загадочный дизайн: Новая коллекция 'Тёмная элегантность' покоряет мир. Дизайнер создает уникальные наряды, воплощающие загадочность и притягательность тьмы. Звезды уже стремятся воплотить этот стиль на красных дорожках.	100	2023-07-23 05:26:54.168945
3	2	Кот-творец: Известный художник создал свою галерею с картиными, нарисованными его котом. Картины, созданные лапами мурлыки, разошлись на аукционе за суммы, которые шокировали и самого автора	85	2023-07-23 05:27:51.914808
4	2	Необычное явление: Лисы организовали массовый пикет против птиц! Вчера в парке наблюдалась удивительная сцена, когда группа лис собралась возле деревьев с плакатами 'Заравнивайте гнезда, не делайте гнездовий неравенства!' Видимо, они выступают за равноправие всех обитателей природы.	95	2023-07-23 05:28:44.330279
5	2	Кража в магазине: Лиса-шалун украла у продавца 10 кг моркови! На этот раз жертвой хищницы стал местный овощной рынок. Владельцы магазина признали, что такого аппетита у них еще не встречали.	100	2023-07-25 05:29:13.048861
6	2	Великолепный край снов: Лисы осваивают искусство сновидений! Ученые из университета сообщают, что лисы могут контролировать свои сновидения. Это не только делает их смешными героями сказок, но также может дать ключевые понимания об их поведении и мышлении.	70	2023-07-25 05:29:48.107629
7	3	Лисица-археолог: Ученые нашли доказательства того, что лисы вели древнее племенное общество. Копаясь в археологических раскопках, они обнаружили останки лисиц с нашивками и орудиями труда, подтверждающими развитие цивилизации у этих умных зверей	100	2023-07-25 05:31:52.517081
\.


--
-- Data for Name: digest_post; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.digest_post (digest_id, post_id) FROM stdin;
\.


--
-- Name: digest_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.digest_id_seq', 1, false);


--
-- Name: post_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.post_id_seq', 7, true);


--
-- Name: subscription_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.subscription_id_seq', 1, false);


--
-- PostgreSQL database dump complete
--

